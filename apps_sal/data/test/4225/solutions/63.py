(A, B, C, K) = list(map(int, input().split()))
if A >= K:
    print(K)
elif B >= K - A:
    print(A)
else:
    print(A - 1 * (K - A - B))
