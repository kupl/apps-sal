n, m = [int(x) for x in input().split()]
inp = [input() for i in range(n)]
source = [int(x) - 1 for x in input().split()]
dest = [int(x) - 1 for x in input().split()]


def valid(x):
    return True if 0 <= x[0] < n and 0 <= x[1] < m and inp[x[0]][x[1]] == '.' else False


def getn(x):
    toret = []
    y = (x[0] - 1, x[1])
    if valid(y):
        toret.append(y)
    y = (x[0] + 1, x[1])
    if valid(y):
        toret.append(y)
    y = (x[0], x[1] - 1)
    if valid(y):
        toret.append(y)
    y = (x[0], x[1] + 1)
    if valid(y):
        toret.append(y)
    return toret


if source == dest:
    print('YES' if len(getn(dest)) else 'NO')
else:
    dat = False
    dis = 0
    if inp[dest[0]][dest[1]] == 'X':
        inp[dest[0]] = inp[dest[0]][:dest[1]] + '.' + inp[dest[0]][dest[1] + 1:]
        dat = True
    if tuple(dest) in getn(source):
        dis = 1
    vis = [[False] * m for i in range(n)]
    mystak = [source]
    while mystak != []:
        x = mystak.pop()
        if vis[x[0]][x[1]]:
            continue
        vis[x[0]][x[1]] = True
        for i in getn(x):
            mystak.append(i)
#	for i in vis:
#		print(i)
    print('YES' if vis[dest[0]][dest[1]] and (len(getn(dest)) > 1 - dis or dat) else 'NO')
