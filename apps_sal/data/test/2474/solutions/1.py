#import sys
#sys.setrecursionlimit(10**5)
MOD = 10**9+7

# input
N = int(input())
C = list(map(int, input().split()))
    
# process
C.sort(reverse=True)
ans = 0

if N == 1:
    ans = C[0]*2**N
else:
    for i in range(N):
        ans += C[i]*(2+i)

    ans *= 4**(N-1)

# output
print((ans%MOD))

