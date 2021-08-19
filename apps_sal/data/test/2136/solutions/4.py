import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    a = [list(input())[:-1] for _ in range(N)]
    res = []
    if a[0][1] == a[1][0]:
        x = a[0][1]
        if a[-1][-2] == x:
            res.append((N, N - 1))
        if a[-2][-1] == x:
            res.append((N - 1, N))
    elif a[-1][-2] == a[-2][-1]:
        x = a[-1][-2]
        if a[0][1] == x:
            res.append((1, 2))
        if a[1][0] == x:
            res.append((2, 1))
    else:
        x = a[0][1]
        res.append((2, 1))
        if a[-1][-2] == x:
            res.append((N, N - 1))
        if a[-2][-1] == x:
            res.append((N - 1, N))
    print(len(res))
    for r in res:
        print(*r)
