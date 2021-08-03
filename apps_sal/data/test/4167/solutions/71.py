n, k = map(int, input().split())
ans = (n // k)**3
if (k % 2 == 0):
    ans += (n // (k // 2) - n // k)**3
print(ans)
