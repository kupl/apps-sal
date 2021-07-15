from bisect import bisect_left
from itertools import accumulate
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
bs = [0]*N
for i in range(N):
    b = B[i]
    ai = bisect_left(A, b)
    bs[i] = ai
bs = [0]+list(accumulate(bs, lambda x,y:x+y))
ans = 0
for i in range(N):
    c = C[i]
    bi = bisect_left(B, c)
    ans += bs[bi]
print(ans)
