n, k = [int(x) for x in input().split()]
s = input()

start, target = 0, 0
for i, c in enumerate(s):
    if c == 'G':
        start = i
    if c == 'T':
        target = i

visited = set()


def dfs(i):
    if i in visited:
        return False
    if i == target:
        return True
    if not (0 <= i < len(s)) or s[i] == '#':
        return False
    visited.add(i)
    return dfs(i - k) or dfs(i + k)


print('YES' if dfs(start) else 'NO')
