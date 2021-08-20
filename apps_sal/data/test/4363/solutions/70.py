(k, s) = map(int, input().split())
ans = 0
for i1 in range(min(k + 1, s + 1)):
    for i2 in range(0, min(k + 1, s - i1 + 1)):
        if s - (i1 + i2) <= k:
            ans += 1
print(ans)
