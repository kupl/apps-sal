(k, s) = map(int, input().split())
ans = 0
for x in range(k + 1):
    if x > s:
        break
    else:
        for y in range(k + 1):
            if x + y > s:
                break
            elif s - x - y <= k:
                ans += 1
print(ans)
