import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))

"""
ある一塊を見ると，スライドした形にしかならない，という事実はありそう
(14)(25)(36)みたいな

他のものは内包しない．(14)(23)みたいなのはない

なので，埋まる時は区間が埋まっていく，l,rがあって，[l,r)が全て一使用済みになる感じ
区間dpできるか?
いや，区間を跨ぐやつどうしよう不可の区間を2つ繋げて可になることがある

入力例1でいうところの(14)がありえないことに注意．
つまり，ABがともに決まっているもの以外，右向き/左向きは，未決定のものと組むしかないのか

なんだか貪欲でできそうな気もする...
(0d)をつなげるか？をやって，できるなら(d+1,x)みたいなことをまたやって，と行けば良い？
あーでも，これ結局区間の情報をdpみたいに持つか，メモ化?

区間を決めたとき，その区間内でOKかどうかを決めるのはめんどいけど，
その区間が一塊になれるかどうかの判定は楽(左右が決まれば組み方は一意)

これを全ての[l,r)で試せば良い

"""
def main():
    mod=10**9+7
    N=I()
    st=[0]*(2*N) # 不明:0，左向き:-1，　右向き:1　　(ただし相方が確定済みの人は0とする)
    flag=1
    looked=[]#乗り降りする階が被ってはいけない
    
    fixed=[-1]*(2*N) #確定した相方がどこにいるか，いなければ-1
    
    for i in range(N):
        a,b=MI()
        a-=1
        b-=1
        if a!=-2:
            looked.append(a)
        if b!=-2:
            looked.append(b)
            
        
        if a!=-2 and b!=-2:#相方確定
            fixed[a]=b
            fixed[b]=a
            if b<=a:#上の階から乗ってくる人がいたら不可
                flag==0
        else:
            #向きをセット
            if a!=-2:
                st[a]=1
            if b!=-2:
                st[b]=-1
            
    looked.sort()
    for i in range(len(looked)-1):
        aa=looked[i]
        bb=looked[i+1]
        if aa==bb:
            flag=0
            
    if flag==0:
        print("No")
        return
        
    from collections import defaultdict
    dd = defaultdict(int)
    
    def check(a,d):
        # aを左端として，(a,a+d)を結べるか
        
        if a+2*d-1>=2*N:# オーバー
            return False
        
        for i in range(d):#aから何ます右に行ったところから開始するか
            # lとrを結ぶ
            l=a+i
            r=l+d
            
            # print(l,r)
            
            if fixed[l]!=-1:# lに確定相方がいるなら
                if fixed[l]!=r:# rじゃないとだめ
                    return False
            elif fixed[r]!=-1:# rに確定相方がいるなら
                if fixed[r]!=l:# lじゃないとだめ
                    return False
            else:#　lもrも相方が未定
                # lは左を向いてはいけない
                if st[l]==-1:
                    return False
                # rは右を向いてはいけない
                if st[r]==1:
                    return False
                
                # 一見良さそうだけど，違う人同士を結ばないとだめ，どちらかは0出なければならない
                if st[l] * st[r] != 0:
                    return False
        return True
                
            
    # [l,r)でひとまとめにできるところを有向辺で繋ぐ，0から2Nまで行けたらOK
    adj=[[]for _ in range(2*N+1)]
    for i in range(2*N):
        for d in range(1,N+3):
            if (i+2*d)<=2*N:
               if check(i,d):
                    adj[i].append(i+2*d)
                
    can=[0]*(2*N+1)
    can[0]=1
    
    import queue
    q=queue.Queue()
    q.put(0)
    
    while not q.empty():
        v=q.get()
        for nv in adj[v]:
            if can[nv]==0:
                can[nv]=1
                q.put(nv)
                
    # print(st)
    # print(fixed)
    # print(adj)        
    
    if can[-1]:
        print("Yes")
    else:
        print("No")
            

  
        
    

main()

