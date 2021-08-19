(k, s) = map(int, input().split())
cnt = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - (x + y)
        if 0 <= z <= k and x + y + z == s:
            cnt += 1
print(cnt)
