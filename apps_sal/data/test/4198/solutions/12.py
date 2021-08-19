(A, B, X) = map(int, input().split())
ans = 0
for d in range(1, 19):
    if X - B * d <= 0:
        break
    N = min((X - B * d) // A, 10 ** d - 1)
    ans = max(ans, N)
print(min(ans, 10 ** 9))
