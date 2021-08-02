t = int(input())

for _ in range(t):
    n = int(input())
    B = [input() for _ in range(n)]
    a, b = list(map(int, (B[0][1], B[1][0])))
    c, d = list(map(int, (B[-1][-2], B[-2][-1])))

    ans = []
    if abs(a - 1) + abs(b - 1) + abs(c - 0) + abs(d - 0) <= 2:
        if a == 0:
            ans.append((1, 2))
        if b == 0:
            ans.append((2, 1))
        if c == 1:
            ans.append((n, n - 1))
        if d == 1:
            ans.append((n - 1, n))
    else:
        if a == 1:
            ans.append((1, 2))
        if b == 1:
            ans.append((2, 1))
        if c == 0:
            ans.append((n, n - 1))
        if d == 0:
            ans.append((n - 1, n))
    print(len(ans))
    for p in ans:
        print(*p)
