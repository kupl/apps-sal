import sys
sys.setrecursionlimit(10 ** 5 + 10)
(N, A, B, C) = [int(i) for i in input().split()]
ans = list()
l = list()
for n in range(N):
    l.append(input())


def dfs(i, a, b, c):
    if i == N:
        return True
    ss = l[i]
    if ss == 'AB':
        if a == 0 and b == 0:
            return False
        if b > 0 and dfs(i + 1, a + 1, b - 1, c):
            ans.append('A')
            return True
        if a > 0 and dfs(i + 1, a - 1, b + 1, c):
            ans.append('B')
            return True
    if ss == 'AC':
        if a == 0 and c == 0:
            return False
        if c > 0 and dfs(i + 1, a + 1, b, c - 1):
            ans.append('A')
            return True
        if a > 0 and dfs(i + 1, a - 1, b, c + 1):
            ans.append('C')
            return True
    if ss == 'BC':
        if b == 0 and c == 0:
            return False
        if c > 0 and dfs(i + 1, a, b + 1, c - 1):
            ans.append('B')
            return True
        if b > 0 and dfs(i + 1, a, b - 1, c + 1):
            ans.append('C')
            return True
    return False


dfs(0, A, B, C)
if len(ans) > 0:
    print('Yes')
    for x in reversed(ans):
        print(x)
else:
    print('No')
