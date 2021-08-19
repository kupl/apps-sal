from itertools import permutations


def dfs(x):
    r = x == 0
    while x:
        r += 1
        x //= 7
    return r


(n, m) = list(map(int, input().split()))
(res, ln, lm) = (0, dfs(n - 1), dfs(m - 1))
for i in permutations('0123456', ln + lm):
    i = ''.join(i)
    res += int(i[:ln], 7) < n and int(i[ln:], 7) < m
print(res)
