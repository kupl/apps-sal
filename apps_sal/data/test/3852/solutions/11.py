"""
xとyが同じでもよいことに注意。
それぞれに自分以外の数を全部足したら、全部同じ数になるな。それも一つの正解か？
まずA1に、O(N-1)回で自分以外の数を全部足す。
次に、A2に+A1の2回で同様に同じ数にする。ってやると全体でO(2N-2+N-1)=O(3N-3)かかるな。

同じ数にするのはハードル高くても、昇順なら
一番左から昇順に直していく。

全部0以上にするか、全部0以下にするかしたい。
全部正にしたら左から累積和。
全部負にしたら右から累積和を取れば正解にになる。

そのためにはセットアップが必要。
初期状態で最大値と最小値を探す。
最大値も最小値も0以上あるいは、最大値も最小値も0以下ならセットアップ不要。
最大値が0以上、最小値が負の値の時はセットアップが必要。
abs(最大値) >= abs(最小値)なら全部に最大値を加える。
abs(最大値) < abs(最小値)なら全部に最小値を加える。

こうすることで、数列を正の値か負の値どちらかにそろえることができる。
"""
N = int(input())
A = list(map(int,input().split()))
MAX = max(A)
MIN = min(A)
MAXidx = A.index(MAX)+1
MINidx = A.index(MIN)+1

def positiveOpe():
    for i in range(1,N):
        print((i,i+1))

def negativeOpe():
    for i in range(N,1,-1):
        print((i,i-1))

if MIN >= 0:
    print((N-1))
    positiveOpe()
elif MAX <= 0:
    print((N-1))
    negativeOpe()
elif abs(MAX) >= abs(MIN):
    print((N-1+N))
    for i in range(1,N+1):
        print((MAXidx,i))
    positiveOpe()
else:
    print((N-1+N))
    for i in range(1,N+1):
        print((MINidx,i))
    negativeOpe()

