n, q = map(int, input().split())

fr = dict()
for i in range(q):
    a, b = input().split()
    if b in fr:
        fr[b].append(a)
    else:
        fr[b] = [a]


def dfs(c, cnt):
    nonlocal n
    if cnt == n:
        return 1
    if cnt > n:
        return 0
    
    nonlocal fr
    if c not in fr:
        return 0
    
    ans = 0
    for i in fr[c]:
        ans += dfs(i[0], cnt+1)
    return ans


print(dfs('a', 1))
