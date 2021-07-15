import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

t, r = divmod(A[-1], 2)
idx = bisect.bisect_left(A, t)

if r == 1:
    if idx != 0:
        if abs(A[idx - 1] - t) < abs(A[idx] - t):
            idx = idx - 1
else:
    if idx != 0:
        if abs(A[idx - 1] - t) <= abs(A[idx] - t):
            idx = idx - 1

print((' '.join([str(A[-1]), str(A[idx])])))


