import sys

n, m = list(map(int, input().split()))
mex = n
for line in sys.stdin:
    l, r = list(map(int, line.split()))
    mex = min(mex, r-l+1)

A = [i%mex for i in range(n)]
print(mex)
print(' '.join(map(str, A)))

