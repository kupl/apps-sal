# https://codeforces.com/problemset/problem/886/D
def is_all_used(used):
    for val in list(used.values()):
        if val != True:
            return False
    return True


def is_circle(d, pre):
    used = {x: False for x in d}
    pre_none = [x for x in used if x not in pre]
    s_arr = []

    for x in pre_none:
        cur = []
        flg = dfs(x, d, used, cur)

        if flg == True:
            return True, None

        s_arr.append(cur)

    if is_all_used(used) != True:
        return True, None

    return False, s_arr


def dfs(u, d, used, cur):
    used[u] = True
    cur.append(u)
    flg = False

    for v in d[u]:
        if used[v] == True:
            return True

        flg = dfs(v, d, used, cur)

        if flg == True:
            return flg
    return flg


def push(d, u, v=None):
    if u not in d:
        d[u] = set()

    if v is not None:
        if v not in d:
            d[v] = set()
        d[u].add(v)


def push_p(d, v):
    if v not in d:
        d[v] = 0
    d[v] += 1


def is_deg_valid(d):
    for u in d:
        if len(d[u]) > 1:
            return True
    return False


def solve():
    n = int(input())
    d = {}
    pre = {}

    for _ in range(n):
        s = input()
        if len(s) == 1:
            push(d, s)
        else:
            for u, v in zip(s[:-1], s[1:]):
                push(d, u, v)
                push_p(pre, v)

    flg, arr = is_circle(d, pre)

    if is_deg_valid(d) or flg == True:
        return 'NO'

    S = [''.join(x) for x in arr]
    S = sorted(S)
    return ''.join([s for s in S])


print(solve())

# 4
# mail
# ai
# lru
# cf

# 3
# kek
# preceq
# cheburek
