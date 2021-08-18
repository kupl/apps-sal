from fractions import gcd


def dfs(cur, sz):
    used[cur] = True
    v = a[cur]
    if (used[v]):
        return sz + 1
    else:
        return dfs(v, sz + 1)


n = int(input())


def nok(a, b):
    return (a * b) // gcd(a, b)


a = list(map(int, input().split()))
par = [-1] * n
for i in range(len(a)):
    a[i] -= 1
    if par[a[i]] != -1:
        print(-1)
        return
    else:
        par[a[i]] = i
# print(par)
used = [False] * n
curnok = 1
for i in range(n):
    if (not used[i]):
        cur = dfs(i, 0)
        if cur % 2 == 0:
            cur //= 2
        curnok = nok(curnok, cur)
print(curnok)
