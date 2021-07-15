N, M = map(int, input().split())

A = list(map(int, input().split()))

print("-1" if N - sum(A) < 0 else N - sum(A))
