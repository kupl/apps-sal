n = int(input())
ans = 0
i = 1
while i <= n:
    j = 1
    cnt = 0
    while j <= i:
        if i % j == 0:
            cnt += 1
        j += 1
    if cnt == 8 and i % 2 == 1:
        ans += 1
    i += 1
print(ans)
