l, r = map(int, input().split())
m = 2019
for i in range(l, min(r + 1, l + 2020)):
    for j in range(i + 1, min(r + 1, l + 2020)):
        i %= 2019
        j %= 2019
        m = min(m, (i * j) % 2019)
print(m % 2019)
