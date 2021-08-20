def isPrefix(sa, sb):
    if len(sa) >= len(sb):
        return False
    return sa == sb[0:len(sa)]


def getOrder(sa, sb):
    for i in range(min(len(sa), len(sb))):
        if sa[i] != sb[i]:
            return (sa[i], sb[i])


test = False
if test:
    fp = open('in.txt', 'r')
    n = int(fp.readline().strip())
    names = [fp.readline().strip() for _ in range(n)]
    fp.close()
else:
    n = int(input().strip())
    names = [input().strip() for _ in range(n)]
res = True
g = [[False] * 26 for _ in range(26)]
'\nfor i in range(26):\n    for j in range(26):\n        g[i][j] = False\n'


def printG():
    print(' abcdefghijklmnopqrstuvwxyz')
    for i in range(0, 26):
        print(chr(ord('a') + i), ''.join(['1' if x else '0' for x in g[i]]), sep='')


for i in range(n - 1):
    if names[i] == names[i + 1] or isPrefix(names[i], names[i + 1]):
        continue
    elif isPrefix(names[i + 1], names[i]):
        res = False
        break
    else:
        (ca, cb) = getOrder(names[i], names[i + 1])
        if g[ord(cb) - ord('a')][ord(ca) - ord('a')]:
            res = False
            break
        else:
            a = ord(ca) - ord('a')
            b = ord(cb) - ord('a')
            g[a][b] = True
if not res:
    print('Impossible')
else:

    def getZeroIndegreeNode():
        for i in range(26):
            if not vis[i] and Indegree[i] == 0:
                return i
        return -1
    strOrder = []
    vis = [False] * 26
    Indegree = [0] * 26
    for i in range(26):
        ithIndegree = 0
        for j in range(26):
            if g[j][i]:
                ithIndegree += 1
        Indegree[i] = ithIndegree
    for i in range(26):
        ZeroIndegreeNode = getZeroIndegreeNode()
        if ZeroIndegreeNode == -1:
            res = False
            break
        else:
            strOrder.append(chr(ord('a') + ZeroIndegreeNode))
            vis[ZeroIndegreeNode] = True
            for i in range(26):
                if g[ZeroIndegreeNode][i]:
                    Indegree[i] -= 1
    if not res:
        print('Impossible')
    else:
        print(''.join(strOrder))
