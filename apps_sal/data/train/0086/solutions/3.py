t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n // 2):
        if a[i * 2] == 1 and a[i * 2 + 1] == 1:
            res.append(1)
            res.append(1)
        elif a[i * 2] == 0 and a[i * 2 + 1] == 0:
            res.append(0)
            res.append(0)
        else:
            res.append(0)
    print(len(res))
    print(*res)
