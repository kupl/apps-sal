L, R = map(int, input().split())


if R - L >= 2018:
    print(0)
else:
    m = 2019
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            m = min(m, i * j % 2019)
    print(m)
