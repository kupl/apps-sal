import sys
sys.setrecursionlimit(10 ** 6)
(n, A, B, C) = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
inf = 10 ** 9
'\n解法\nそれぞれの竹について「Aの材料」、「Bの材料」、「Cの材料」、「使わない」の4択を決める(4**n通り)\n'


def dfs(cur, a, b, c):
    if cur == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else inf
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
