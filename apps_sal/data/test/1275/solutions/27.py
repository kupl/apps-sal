n, k = map(int, input().split())

ans = 0
for A in range(2, 2 * n + 1):
    B = A - k
    if 2 <= B <= 2 * n:
        ans += min(A - 1, 2 * n + 1 - A) * min(B - 1, 2 * n + 1 - B)

print(ans)
