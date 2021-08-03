L, R = map(int, input().split())
l1 = L // 2019
r1 = R // 2019
if l1 < r1:
    print(0)
elif l1 == r1:
    res = []
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            res.append((i * j) % 2019)
    print(min(res))
