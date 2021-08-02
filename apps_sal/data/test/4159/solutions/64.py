A, B, K = map(int, input().split())

if A + B <= K:
    print(0, 0)
elif A <= K:
    print(0, B - (K - A))
else:
    print(A - K, B)
