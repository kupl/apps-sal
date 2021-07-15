n, k = map(int, input().split())
ans = 0
for b in range(k + 1, n + 1):
    temp = n // b
    temp2 = n % b
    ans += temp * (b - k) + max(temp2 - max(0, (k - 1)), 0)
print(ans)
