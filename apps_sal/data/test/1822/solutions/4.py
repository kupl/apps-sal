import sys
sys.setrecursionlimit(100000)
def solve():
    n, x, = rv()
    x -= 1
    a, = rl(1)
    a = [val - 1 for val in a]
    nxt = [True] * n
    index = [-1] * n
    for i in range(len(a)):
        index[i] = get(i, a, nxt)
    curindex = index[x] - 1
    others = list()
    for i in range(n):
        if not bad(i, a, x) and nxt[i]:
            others.append(index[i])
    others.sort()
    possible = [False] * (n + 1)
    possible[0] = True
    for val in others:
        pcopy = list(possible)
        for i in range(n + 1):
            if possible[i]:
                both = i + val
                if both < n + 1:
                    pcopy[both] = True
        possible = pcopy
    res = list()
    for i in range(n + 1):
        if possible[i]:
            comb = i + curindex
            if comb < n:
                res.append(comb)
    print('\n'.join(map(str, [val + 1 for val in res])))

def bad(index, a, x):
    if index == x: return True
    if a[index] == x: return True
    if a[index] == -1: return False
    return bad(a[index], a, x)

def get(index, a, nxt):
    if a[index] == -1:
        return 1
    else:
        nxt[a[index]] = False
        return get(a[index], a, nxt) + 1

def prt(l): return print(' '.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()
