import re
n = int(input())
MOD = 10**9 + 7

string = "ACGT"

# AGC
# A*GC
# GAC
# ACG
# AG*C

table = [{} for i in range(n + 1)]


def dfs(s="", depth=n):
    if table[depth].get(s) is not None:
        return table[depth][s]
    if re.search(r"(AGC|A.GC|GAC|ACG|AG.C)", s):
        table[depth][s] = 0
        return 0
    if depth == 0:
        table[depth][s] = 1
        return 1

    cnt = 0
    for i in string:
        cnt += dfs(s[-3:] + i, depth - 1)
        if cnt >= MOD:
            cnt %= MOD
    table[depth][s] = cnt
    return cnt


print((dfs()))
