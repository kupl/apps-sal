for _ in range(int(input())):
    n = int(input())
    hold = n
    res = []
    for i in range(n - 1, 0, -1):
        res.append((hold, i))
        hold = (hold + i + 1) // 2
    print(hold)
    for i in res:
        print(*i)
