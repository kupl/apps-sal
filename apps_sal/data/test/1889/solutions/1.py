n, m, q = list(map(int, input().split()))

s = []
t = []


def getMax(line):
    cur = 0
    res = 0
    for v in line:
        if v == 1:
            cur += 1
        else:
            res = max(res, cur)
            cur = 0
    res = max(res, cur)
    return res


for i in range(n):
    si = list(map(int, input().split()))
    s.append(si)
    t.append(getMax(si))

# res = max(t)

# print(t)

for qi in range(q):
    i, j = list(map(int, input().split()))
    s[i - 1][j - 1] = int(not s[i - 1][j - 1])
    t[i - 1] = getMax(s[i - 1])
    # print(t)
    res = max(t)
    print(res)
