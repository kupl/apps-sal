A, B, C, K = list(map(int, input().split()))

ans = 0
if A > K:
    print(K)
elif A == K:
    print(A)
elif A + B >= K:
    print(A)
else:
    print(A - (K - A - B))
