import sys
sys.setrecursionlimit(10000000)
'\n違反文字列\nAGC -> AGときたらCはNG\nGAC -> GAときたらCはNG\nACG -> ACときたらGはNG\nAQGC-> A*GときたらCはNG\nAGQC-> AG*ときたらCはNG\n'
n = int(input())
p = 10 ** 9 + 7
ok = ['A', 'G', 'C', 'T']
ng = ['AGC', 'GAC', 'ACG']
memo = [{} for i in range(n + 1)]


def check(text):
    if text[1:] in ng:
        return 0
    if text[:2] == 'AG' and text[3] == 'C' or (text[0] == 'A' and text[2:] == 'GC'):
        return 0
    return 1


def dfs(cnt, last):
    if last in memo[cnt]:
        return memo[cnt][last]
    if cnt == n:
        return 1
    ans = 0
    for o in ok:
        if check(last + o):
            ans += dfs(cnt + 1, last[1:] + o) % p
    memo[cnt][last] = ans
    return ans % p


print(dfs(0, 'TTT') % p)
