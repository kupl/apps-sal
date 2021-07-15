for _ in range(int(input())):
    n = int(input())
    d = 1
    res = [0]
    while d <= n:
        e = n // d
        res.append(e)
        d = (n // e) + 1
    print(len(res))
    print(*sorted(res))
