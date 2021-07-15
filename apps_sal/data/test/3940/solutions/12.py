import sys

n, m = list(map(int, input().split()))
mex = n
for i in range(m):
    l, r = list(map(int, input().split()))
    mex = min(mex, r-l+1)

A = [i%mex for i in range(n)]
print(mex)
print(' '.join(map(str, A)))

