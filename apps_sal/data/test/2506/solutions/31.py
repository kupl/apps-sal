import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return list(map(int,input().split()))
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    if len(x) == 0:
        return []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(list(map(max,x)))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans






N,M = m()

a = l()

a.sort()

aaa = s(a)



po = [0 for i in range(10**5+2)]
ans = 0
for i in range(N):
    po[a[i]] += 1
for i in range(10**5,-1,-1):
    po[i] += po[i+1]
ll = 0
rr = 10**5 * 2 + 1

while True:
    mid = (ll+rr)//2
    if mid == ll:
        co = 0
        for i in range(N):
            ui = a[i]
            if mid > ui + 10**5:
                continue
            elif ui >= mid:
                co += N
            else:
                co += po[mid-ui]
        cco = 0
        mid = rr

        for i in range(N):
            ui = a[i]
            if mid > ui + 10**5:
                continue
            elif ui >= mid:
                cco += N
            else:
                cco += po[mid-ui]

        if cco == M:
            mid = rr
            co=cco

        else:
            mid = ll

        break

    co = 0
    for i in range(N):
        ui = a[i]
        if mid > ui + 10**5:
            continue
        elif ui >= mid:
            co += N
        else:
            co += po[mid-ui]
    
    if co < M:
        rr = mid                 
    else:
        ll = mid


a.sort(reverse = True)
dp = [0]

ans -= mid * (co - M)



for i in range(N):
    dp.append(dp[-1]+a[i])

for i in range(N):
    pl = a[i]
    if pl >= mid:
        ans += pl*N + dp[-1]
        
    elif pl + 10**5 < mid:
        continue
    else:
        ans += pl*po[mid-pl] + dp[po[mid-pl]]
print(ans)




