n, k = map(int, input().split())
ans = 0
if k >= 1:
    ans += 1
if k >= 2:
    ans += n * (n - 1) // 2
if k >= 3:
    ans += n * (n - 1) * (n - 2) // 3
if k >= 4:
    ans += n * (n - 1) * (n - 2) * (n - 3) // (4 * 3 * 2 * 1) * 9
print(ans)
