n, k = map(int, input().split())
ans = 0
if k % 2 == 0:
    ans += ((n + k // 2) // k)**3
ans += (n // k)**3
print(ans)
