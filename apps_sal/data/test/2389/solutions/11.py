import sys
sys.setrecursionlimit(10**7)
ans = ''


def dfs(a, b, c, t):
    nonlocal ans
    if a < 0 or b < 0 or c < 0:
        return False
    if t == N:
        return True
    if s[t] == 'AB':
        if dfs(a - 1, b + 1, c, t + 1):
            ans += 'B'
            return True
        elif dfs(a + 1, b - 1, c, t + 1):
            ans += 'A'
            return True
    if s[t] == 'BC':
        if dfs(a, b - 1, c + 1, t + 1):
            ans += 'C'
            return True
        elif dfs(a, b + 1, c - 1, t + 1):
            ans += 'B'
            return True
    if s[t] == 'AC':
        if dfs(a + 1, b, c - 1, t + 1):
            ans += 'A'
            return True
        if dfs(a - 1, b, c + 1, t + 1):
            ans += 'C'
            return True
    return False


N, A, B, C = map(int, input().split())
s = [input() for i in range(N)]

if dfs(A, B, C, 0):
    print('Yes')
    print(*ans[::-1], sep='\n')
else:
    print('No')
