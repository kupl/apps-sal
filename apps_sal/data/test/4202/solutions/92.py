(l, r) = map(int, input().split())
ans = 2018 ** 2
for i in range(l, min(r, l + 2019)):
    v = i % 2019
    for j in range(l + 1, min(r + 1, l + 2020)):
        w = j % 2019
        ans = min(ans, v * w % 2019)
print(ans)
