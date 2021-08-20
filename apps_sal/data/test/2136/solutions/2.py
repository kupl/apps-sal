l = [(1, 0), (0, 1), (-1, -2), (-2, -1)]
t = int(input())
for _ in range(t):
    n = int(input())
    s = [input() for _ in range(n)]
    cnt = 0
    for (x, y) in l:
        if (s[x][y] == '1') ^ (x >= 0):
            cnt += 1
    if cnt >= 2:
        print(4 - cnt)
        for (x, y) in l:
            if (s[x][y] == '1') ^ (x < 0):
                print(x % n + 1, y % n + 1)
    else:
        print(cnt)
        for (x, y) in l:
            if (s[x][y] == '1') ^ (x >= 0):
                print(x % n + 1, y % n + 1)
