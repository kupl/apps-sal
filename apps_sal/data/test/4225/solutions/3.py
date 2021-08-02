A, B, C, K = list(map(int, input().split()))

if A >= K:
    ans = K
elif A + B >= K and A < K:
    ans = A
elif A + B < K:
    ans = 2 * A + B - K

print(ans)
