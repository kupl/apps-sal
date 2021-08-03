A, B, K = map(int, input().split())
if A >= K:
    ans_a = A - K
    ans_b = B
elif A < K and A + B >= K:
    K = K - A
    ans_a = 0
    ans_b = B - K
else:
    ans_a = 0
    ans_b = 0
print(str(ans_a) + " " + str(ans_b))
