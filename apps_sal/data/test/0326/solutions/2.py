from heapq import heapify, heappop, heappush


def rolling(s):
    """
    文字列 [i, j] のハッシュ
    j < i の場合は逆順
    """
    n = len(s)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        rh = 0
        for j in range(i, n):
            b = ord(s[j]) - 96
            rh = rh * 27 + b
            ret[i][j] = rh

    for j in range(n):
        rh = 0
        for i in range(j, -1, -1):
            b = ord(s[i]) - 96
            rh = rh * 27 + b
            ret[j][i] = rh

    return ret


def solve(n, sss, ccc, rhs):
    INF = 10 ** 18
    ans = INF
    q = []
    for i in range(n):
        s = sss[i]
        c = ccc[i]
        l = len(s)

        q.append((c, 0, i, 0))
        q.append((c, 1, i, l - 1))

        for j in range(l):
            k = 1
            while j - k >= 0 and j + k < l:
                if s[j - k] != s[j + k]:
                    break
                k += 1
            else:
                if j - k == -1 and j + k == l:
                    ans = min(ans, c)
                elif j - k == -1:
                    q.append((c, 0, i, j + k))
                else:
                    q.append((c, 1, i, j - k))

        for j in range(l - 1):
            k = 0
            while j - k >= 0 and j + k + 1 < l:
                if s[j - k] != s[j + k + 1]:
                    break
                k += 1
            else:
                if j - k == -1 and j + k + 1 == l:
                    ans = min(ans, c)
                elif j - k == -1:
                    q.append((c, 0, i, j + k + 1))
                else:
                    q.append((c, 1, i, j - k))

    heapify(q)

    checked = []
    for s in sss:
        checked.append([[False, False] for _ in range(len(s))])

    while q:
        cost, fb, i, j = heappop(q)
        if cost >= ans:
            break
        if checked[i][j][fb]:
            continue
        s = sss[i]
        ls = len(s)
        lm = ls - j if fb == 0 else j + 1
        checked[i][j][fb] = True
        rhr = rhs[i][j]

        if fb == 0:
            for ti in range(n):
                t = sss[ti]
                lt = len(t)
                if lm == lt:
                    if rhs[ti][-1][0] == rhr[-1]:
                        ans = min(ans, cost + ccc[ti])
                elif lm > lt:
                    if rhs[ti][-1][0] == rhr[j + lt - 1]:
                        heappush(q, (cost + ccc[ti], 0, i, j + lt))
                else:
                    if rhs[ti][-1][lt - lm] == rhr[-1]:
                        heappush(q, (cost + ccc[ti], 1, ti, lt - lm - 1))
        else:
            for ti in range(n):
                t = sss[ti]
                lt = len(t)
                if lm == lt:
                    if rhs[ti][0][-1] == rhr[0]:
                        ans = min(ans, cost + ccc[ti])
                elif lm > lt:
                    if rhs[ti][0][-1] == rhr[j - lt + 1]:
                        heappush(q, (cost + ccc[ti], 1, i, j - lt))
                else:
                    if rhs[ti][0][lm - 1] == rhr[0]:
                        heappush(q, (cost + ccc[ti], 0, ti, lm))

    if ans == INF:
        return -1
    else:
        return ans


n = int(input())
sss = []
ccc = []
rhs = []
for si in range(n):
    s, c = input().split()
    sss.append(s)
    ccc.append(int(c))
    rhs.append(rolling(s))

print((solve(n, sss, ccc, rhs)))
