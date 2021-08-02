k, s = map(int, input().split())

cnt = 0
for x in range(k + 1):
    for y in range(k + 1):
        if x + y <= s:
            z = s - (x + y)
            if z <= k:
                cnt += 1

print(cnt)
