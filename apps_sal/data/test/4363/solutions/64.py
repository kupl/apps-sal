(k, s) = list(map(int, input().split()))
ans = 0
for x in range(k + 1):
    for y in range(k + 1):
        tmp = s - x - y
        if 0 <= tmp and tmp <= k:
            ans += 1
print(ans)
