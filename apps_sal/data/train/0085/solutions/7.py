def solve():
    s = list(map(int, input()))
    n = len(s)
    x = int(input())
    w = [0] * n
    d = [False] * n
    for i in range(n):
        if s[i] == 0:
            if i - x >= 0:
                w[i - x] = 0
                d[i - x] = True
            if i + x < n:
                w[i + x] = 0
                d[i + x] = True
    for i in range(n):
        if not d[i]:
            w[i] = 1
            d[i] = True
    t = [0] * n
    for i in range(n):
        if i - x >= 0 and w[i - x] == 1:
            t[i] = 1
        if i + x < n and w[i + x] == 1:
            t[i] = 1
    if s != t:
        print('-1')
        return
    print(''.join(map(str, w)))
t = int(input())
for _ in range(t):
    solve()
