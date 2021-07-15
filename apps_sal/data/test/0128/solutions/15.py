n, k = list(map(int, input().split()))

ans = 0

cur = 1
left = n
while k > 0 and cur <= n // 2:
    ans += left + left - 3
    left -= 2
    cur += 1
    k -= 1

print(ans)

