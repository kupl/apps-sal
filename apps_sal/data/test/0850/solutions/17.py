from sys import stdin


def read():
    return list(map(int, stdin.readline().split()))


(n,) = read()
g = [-1 for i in range(8)]
for x in read():
    m = 0
    if x % 10 != 0:
        m += 1
    if x // 10 % 10 != 0:
        m += 2
    if x // 100 != 0:
        m += 4
    g[m] = x
ans = []
for startM in range(8):
    if g[startM] >= 0:
        curA = [g[startM]]
        curM = startM
        for m in [0, 1, 2, 4, 3, 6, 5, 7]:
            if m != startM and g[m] >= 0 and (curM & m == 0):
                curM |= m
                curA.append(g[m])
        if len(curA) > len(ans):
            ans = curA
print(len(ans))
print(' '.join(map(str, ans)))
