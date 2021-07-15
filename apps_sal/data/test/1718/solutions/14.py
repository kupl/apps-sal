n,k = map(int,input().split())
a = list(map(int,input().split()))

if k == n:
    print(1)
    return
if k == 1:
    print(n)
    return

ans = 1
n -= k
if n%(k-1) == 0:
    print(ans + n//(k-1))
else:
    print(ans+1+n//(k-1))
