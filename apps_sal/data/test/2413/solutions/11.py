for _ in range(int(input())):
    n = int(input())
    u = list(map(int, list(input())))
    if u[:] == [0] * n:
        print(n)
        continue
    a = -1; b = -1
    for i in range(n):
        if u[i] == 1:
            a = i
            break
    for i in range(n - 1, -1, -1):
        if u[i] == 1:
            b = i
            break
    print(max((n - a) * 2, (b + 1) * 2, n))
