import sys
input = sys.stdin.readline
def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()


t = getInt()
for _ in range(t):
    n = getInt()
    s = getStr()
    d = {}
    d['0/0'] = 0
    x = 0
    y = 0
    res = [0, n + 1]
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        if s[i] == 'R':
            x += 1
        if s[i] == 'U':
            y += 1
        if s[i] == 'D':
            y -= 1
        k = str(x) + '/' + str(y)
        if k not in d:
            d[k] = i + 1
        else:
            if i + 1 - d[k] < res[1] - res[0]:
                res = [d[k] + 1, i + 1]
            d[k] = i + 1
    if res[1] == n + 1:
        print(-1)
    else:
        print(*res)
