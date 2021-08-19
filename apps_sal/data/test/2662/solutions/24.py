from bisect import bisect_left
N = int(input())
A = []
for _ in range(N):
    x = int(input())
    idx = bisect_left(A, x)
    if idx == 0:
        A.insert(idx, x)
    elif A[idx - 1] == x:
        A.insert(idx, x)
    else:
        A[idx - 1] = x
print(len(A))
