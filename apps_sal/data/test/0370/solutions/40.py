#コメントで解説を書いてみる

#itertoolsとはpythonで組み合わせ全探索するのに使える
import itertools

#標準入力からデータを受け取る
K=int(input())
X,Y=list(map(int,input().split()))

#Mdistとは(0,0)から(X,Y)へのマンハッタン距離
Mdist=abs(X)+abs(Y)
#ここで答えが-1になる条件を考えてみる。
#K:偶数ならマンハッタン距離が偶数の点にしか行けない
#よってKが偶数でMdistが奇数ならその点に行くことができないので答えは-1となる。
if Mdist%2==1 and K%2==0:
    print((-1))
    return

#逆にKが偶数ならマンハッタン距離が偶数の任意の点に行ける
#実際に,(0,0)->(K,0)->(1,1)とすれば点(1,1)に行けるのでこの操作を組み合わせれば良い

#また、K:奇数なら理論上どこでも行ける
#実際に以下の様にすることで(1,0)に行くことができるのでこの操作を組み合わせれば良い
#(0,0)->(2n+1,0)->(n+1,n+1)->(1,0)

#よってこれ以外のパターンは全部可能

#以降は操作を具体的に構成することを考える
#近くになるまで貪欲に進んでいって、近くなったら付近の都合の良い点を探すことを考える

#よってMdist<=2Kの状態でまず考える.
#操作を2回繰り返せばMdist<=2KかつMdist:偶数の任意の点に行ける
#Mdist<=2KでMdist:奇数の点については一回操作をしてから上記の2回の操作を適用すればよい

#よってMdist<=2Kなら3回以内で行けるはず
#Mdist:偶数なら2回、Mdist:奇数なら3回となるが、
#一回で行ける状況を始めに処理しておかないとコーナーケースでエラーになる

#コーナーケースの例:
#5
#1 4

#このケースについては
#1
#1 4
#と出力しなくてはいけないが,
#3
#5 0
#1 -1
#1 4
#と最適でない方法を出力する可能性がある.

if abs(X)+abs(Y)==K:
    print((1))
    print((X,Y))
    return
    
#searchevenとは、Mdist<=2Kの点に行くためにどの点を中継するべきかを出力する
#マンハッタン距離が一定の点の集合は正方形となることから,
#各辺の組み合わせ(4*4通り)について連立方程式を解けば良い
#ここで、2辺が平行になる可能性もあるので,行列式が0になるかならないかで場合分けして考える必要がある。
def searcheven(x,y):
    if abs(x)+abs(y)>2*K:
        return None
    if (abs(x)+abs(y))%2==1:
        return None
    #p1X+p2Y=Kとp3X+p4Y=Kの交点をそれぞれ求める。(pk in {-1,1})
    for ps in itertools.product([-1,1],repeat=4):
        p1,p2,p3,p4=ps
        if p1*p4==p2*p3:
            #並行のときは直線が重なるとき
            #両端のどちらかが条件を満たすのでそれを返す
            if p3*(K-p1*x-p2*y)==-p1*K:
                a,b=0,p4*K
                if abs(x-a)+abs(y-b)==K and abs(a)+abs(b)==K:
                    return (a,b)
                a,b=p3*K,0
                if abs(x-a)+abs(y-b)==K and abs(a)+abs(b)==K:
                    return (a,b)
            else:
                pass
        else:
            #平行でないときは単純に連立方程式を解いている
            tmp1=K-p1*x-p2*y
            tmp2=K
            tmp3=p4*tmp1+p2*tmp2
            tmp4=-p3*tmp1-p1*tmp2
            det=-p1*p4+p2*p3
            a,b=(tmp3//det,tmp4//det)
            #交点が辺の上にあるかをチェックしなければいけない
            if abs(x-a)+abs(y-b)==K and abs(a)+abs(b)==K:
                return (a,b)
            else:
                pass
    return None

#順々に点を移動していく
ans=[(0,0)]
while(True):
    #nx,nyからどこに移動するべきかを決める
    nx,ny=ans[-1]
    if abs(nx-X)+abs(ny-Y)<=2*K:
        #もし近いところに点があるならば先程のsearchevenでどこの点を経由するべきかを決める
        if (abs(nx-X)+abs(ny-Y))%2==0:
            p,q=searcheven(X-nx,Y-ny)
            ans.append((p+nx,q+ny))
            ans.append((X,Y))
            break
        #距離が奇数なら一回別の近傍の点を経由する
        else:
            tmpx=K//2
            tmpy=K-tmpx
            nextkouho=[(tmpx,tmpy),(tmpx,-tmpy),(-tmpx,tmpy),(-tmpx,-tmpy),(K,0),(-K,0),(0,K),(0,-K)]
            for point in nextkouho:
                ptmp,qtmp=point
                p=ptmp+nx;q=qtmp+ny
                if abs(X-p)+abs(Y-q)<=2*K:
                    ans.append((p,q))
                    break
    #遠い場所になるなら距離が近くなるように貪欲に移動する
    #座標がマイナスのときに逆に移動しないように注意
    elif abs(nx)+K<=abs(X):
        if X<0:
            ans.append((nx-K,ny))
            continue
        else:
            ans.append((nx+K,ny))
            continue
    elif abs(ny)+K<=abs(Y):
        if Y<0:
            ans.append((nx,ny-K))
            continue
        else:
            ans.append((nx,ny+K))
            continue


#print(ans)
#これは提出前のデバッグ用
#NGと出力される状況ならふつうにWAになる
s=len(ans)-1
flag=1
for i in range(s):
    ax,ay=ans[i]
    bx,by=ans[i+1]
    if abs(ax-bx)+abs(ay-by)==K:
        pass
    else:
        flag=0
        break
if flag==0:
    print("NG")

#解の出力
#ansには(0,0)データもあるので,それを出力しないように注意
print(s)
for i in range(1,s+1):
    print((ans[i][0],ans[i][1]))

