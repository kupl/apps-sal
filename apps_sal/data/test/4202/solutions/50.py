l, r = map(int, input().split())
ans = 2020
for i in range(l, r):
    for j in range(i + 1, r + 1):
        if (i * j) % 2019 == 0:
            print(0)
            return
        ans = min(ans, (i * j) % 2019)
print(ans)
