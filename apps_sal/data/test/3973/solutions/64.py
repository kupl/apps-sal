import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

n,m = li()
a = list(li_())

ans = [0]*m
# 1.前処理
# 1-1.a[1:]の中の x(0<= x < m)の個数
cnt_equal = [0]*m
for i in range(n-1):
    cnt_equal[a[i+1]] += (((a[i+1]+m-a[i])%m) - 1)

# 1-2.a[i]→a[i+1]の内側(両端除く)に x(0<= x < m)が入る回数
cnt_inner = [0]*(2*m+1)
for i in range(n-1):
    cnt_inner[a[i] + 1] += 1
    cnt_inner[a[i] + (a[i+1]+m-a[i])%m] -= 1
    
cnt_inner = list(accumulate(cnt_inner))
cnt_inner = [cnt_inner[i]+cnt_inner[i+m] for i in range(m)]


# 2.fav == 1 のときのシミュレーション
fav = 0
for i in range(n-1):
    ans[0] += min((a[i+1]+m-a[i])%m, 1+(a[i+1]+m-fav)%m)

# 3.favが[2,m]のとき、fav-1の情報をもとに更新
for fav in range(1,m):
    ans[fav] = ans[fav-1] + cnt_equal[fav-1] - cnt_inner[fav-1]
    
print(min(ans))
