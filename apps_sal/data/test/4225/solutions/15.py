A, B, C, K = list(map(int, input().split()))

if A >= K:
    print(K)
elif A + B >= K:
    print(A)
else:
    print((2 * A + B - K))

