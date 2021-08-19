(A, B, C, X, Y) = list(map(int, input().split()))
ans = 10000000000000
for i in range(0, max(X, Y) + 1):
    ans = min(ans, 2 * i * C + max(0, X - i) * A + max(0, Y - i) * B)
print(ans)
