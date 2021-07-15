l, r = map(int, input().split())

if r - l >= 2019:
    print(0)
else:
    m = 2019
    for i in range(l, r + 1, 1):
        for j in range(i+1, r + 1, 1):
            m = min(i * j % 2019, m)
    print(m)
