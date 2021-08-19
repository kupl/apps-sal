from sys import stdin
input = stdin.readline
(n, m) = list(map(int, input().split()))
s = list(((0, 1)[c == '.'] for c in list(input())))
res = 0
cnt = 0
for k in s:
    if k == 1:
        cnt += 1
    else:
        res += max(cnt - 1, 0)
        cnt = 0
res += max(0, cnt - 1)
for i in range(m):
    (x, c) = input().split()
    x = int(x)
    nc = (0, 1)[c == '.']
    if s[x - 1] != nc:
        diff = 0
        if x < n:
            if s[int(x)] == 1:
                diff += 1
        if x > 1:
            if s[int(x - 2)] == 1:
                diff += 1
        if nc == 1:
            res += diff
        else:
            res -= diff
    s[x - 1] = nc
    print(res)
