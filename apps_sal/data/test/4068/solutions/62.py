n,m = map(int,input().split())
a = set([int(input()) for _ in range(m)])
mod = 10**9+7
fl = [0]*(n+1)
fl[0] = 1

for i in range(1,n+1):
    if i not in a:
        fl[i] = (fl[i-1] + fl[i-2])%mod
    else:
        fl[i] = 0
print(fl[-1])
