for _ in range(int(input())):
    n = int(input())
    l = [*map(int, input().split())]
    res = False
    for i in range(n):
        x = l[i:] + l[:i]
        if all(x[i] < x[i + 1] for i in range(n - 1)) or all(x[i] > x[i + 1] for i in range(n - 1)):
            res = True
    print('YES' if res else 'NO')
