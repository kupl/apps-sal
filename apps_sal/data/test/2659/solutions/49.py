import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)


def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


def ds(n: int):
    return sum([int(i) for i in str(n)])


def snuke(n: int):
    return n / ds(n)


def cands(n: int):
    ret = []
    nl = len(str(n))
    for i in range(nl):
        ret.append(str(n)[:nl - i - 1] + "9" * (i + 1))

    return ret


k = ni()

# 1から9まで
ans = [i for i in range(1, 10)]

# 次の候補
cur = 10
while len(ans) < k:
    cand = cands(cur)
    temp = 10**18
    nex = -1
    for c in cand:
        if snuke(int(c)) <= temp:
            temp = snuke(int(c))
            nex = int(c)

    ans.append(nex)
    cur = nex + 1

for ai in ans[:k]:
    print(ai)
