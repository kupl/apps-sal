import math
import sys
N = int(input())
S = int(input())

def tt(k, N):
    r = 0
    while N:
        N, m = divmod(N, k)
        r += m
#    print(k, r)
    return r

if N == S:
    print((N+1))
    return

for i in range(2, math.floor(N**0.5) + 2):
    if tt(i, N) == S:
        print(i)
        return

for k in range(math.floor(N**0.5), 0, -1):
    s = N//k
    f = N//(k+1) + 1
    si = k + N%k
    fi = si + (s-f)*k
    if N//(s**2) > 0:
        continue
#    print("aaa", k, si, fi, s, f)
    if si <= S <= fi and ((fi-S) % k == 0):
#        print(k)
#        print("cc", f, fi, S, f+(fi-S)//k)
        print((f+(fi-S)//k))
        return
#    for i in range(f, s+1):
#        tt(i, N)
#        if ( i == f or i == s ) and S == tt(i, N):
#            print(i)
#            return

print((-1))

