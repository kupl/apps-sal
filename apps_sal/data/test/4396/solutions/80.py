def resolve():
    n = int(input())
    s = 0
    for _ in range(n):
        x, u = input().split()
        if u == 'BTC':
            s += float(x) * 380000
        else:
            s += float(x) * 1
    print(s)


resolve()
