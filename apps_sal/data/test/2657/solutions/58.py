N = int(input())
A = list(map(int, input().split()))

A_max = max(A)

A.remove(A_max)

X = [abs(a - (A_max // 2)) for a in A]

X_min_id = X.index(min(X))

print(A_max, A[X_min_id])
