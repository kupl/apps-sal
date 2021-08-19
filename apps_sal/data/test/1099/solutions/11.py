import sys
sys.setrecursionlimit(10 ** 5)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def MI1():
    return map(int1, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


n = II()
to = [[] for _ in range(n)]
for _ in range(n - 1):
    (u, v) = MI1()
    to[u].append(v)
    to[v].append(u)
dp = [0] * n
ch = [0] * n
stack = [(0, -1)]
first = [True] * n
while stack:
    (u, pu) = stack.pop()
    if first[u]:
        first[u] = False
        stack.append((u, pu))
        for v in to[u]:
            if v == pu:
                continue
            stack.append((v, u))
    else:
        for v in to[u]:
            if v == pu:
                continue
            ch[u] += 1 + dp[v]
            dp[u] += ch[v]
stack = [(0, -1)]
while stack:
    (u, pu) = stack.pop()
    for v in to[u]:
        if v == pu:
            continue
        dpvu = dp[u] - ch[v]
        chvu = ch[u] - dp[v] - 1
        dp[v] += chvu
        ch[v] += dpvu + 1
        stack.append((v, u))
print(min(dp))
