def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    return x // gcd(x, y) * y


def dfs(x, y):
    if(vis[x]):
        return y
    vis[x] = 1
    return dfs(c[x - 1], y + 1)


n = int(input())
c = []
for x in input().split():
    c.append(int(x))
vis = [0] * (n + 1)
ind = [0] * (n + 1)
for i in range(n):
    ind[i + 1] += 1
    ind[c[i]] += 1
mk = 1
for i in range(n):
    if(ind[i + 1] & 1):
        mk = 0
ans = 1
if(mk):
    for i in range(n):
        if(vis[i + 1] == 0):
            val = dfs(i + 1, 0)
        if(val % 2 == 0):
            val //= 2
        ans = lcm(ans, val)
    print(ans)
else:
    print("-1");
