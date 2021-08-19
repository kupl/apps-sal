import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
As = list(range(N + 1))
Bs = [0] * N
s = 0
for (i, b) in enumerate(B):
    ind = bisect.bisect_left(A, b)
    s += As[ind]
    Bs[i] = s
Bs = [0] + Bs
Cs = [0] * N
ans = 0
for (i, c) in enumerate(C):
    ind = bisect.bisect_left(B, c)
    ans += Bs[ind]
print(ans)
