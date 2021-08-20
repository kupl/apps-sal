(A, B, C, K) = map(int, input().split())
if A >= K:
    print(K)
elif A + B >= K:
    print(A)
elif A + B + C >= K:
    print(A + -1 * (K - A - B))
else:
    print(A - B)
