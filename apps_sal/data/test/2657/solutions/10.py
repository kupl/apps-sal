import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
m = A[-1]
i = bisect.bisect_left(A, m / 2)
if i == 0:
    print(m, A[0])
    return
if i == N - 1:
    print(m, A[-2])
    return
a, b = A[i - 1], A[i]
if abs(a * 2 - m) > abs(b * 2 - m):
    print(m, b)
else:
    print(m, a)
