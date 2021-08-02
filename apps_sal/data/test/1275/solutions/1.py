n, k = map(int, input().split())
ans = 0
for cd in range(2, 2 * n + 1):
    if 2 <= k + cd and k + cd <= 2 * n:
        ans += (n - abs(cd - (n + 1))) * (n - abs((k + cd) - (n + 1)))
print(ans)
