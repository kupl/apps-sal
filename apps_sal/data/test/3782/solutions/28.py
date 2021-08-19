import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


(n, k, q) = MI()
aa = LI()
pp = list(sorted(set(aa)))


def diff(p):
    can = []
    cur = []
    for a in aa + [-1]:
        if a < p:
            if len(cur) == n:
                can = cur
                break
            if len(cur) >= k:
                cur.sort()
                if k == 1:
                    can += cur
                else:
                    can += cur[:-(k - 1)]
            cur = []
        else:
            cur.append(a)
    if len(can) < q:
        return -1
    can.sort()
    res = can[q - 1] - can[0]
    return res


ans = 10 ** 16
for p in pp:
    ret = diff(p)
    if ret == -1:
        break
    ans = min(ans, ret)
print(ans)
