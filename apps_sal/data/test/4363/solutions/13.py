k, s = list(map(int, input().split()))

ans = 0
for x in range(k + 1):
    for y in range(k + 1):
        if 0 <= s - x - y <= k:
            ans += 1

print(ans)
