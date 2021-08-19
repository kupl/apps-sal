from fractions import gcd


def dfs(node):
    if vis[node] == idd[0]:
        return node
    cycleLen[0] += 1
    vis[node] = idd[0]
    return dfs(crush[node])


n = int(input())
crush = list(map(int, input().split()))
for i in range(n):
    crush[i] -= 1
vis = [0] * n
ans = 10 ** 100
idd = [0]
V = []
for i in range(n):
    idd[0] += 1
    cycleLen = [0]
    if dfs(i) != i:
        ans = -1
    V.append(cycleLen[0])
V.sort()


def lcm(x, y):
    return x * y // gcd(x, y)


if ans == -1:
    print(ans)
else:
    ans = 1
    inc = 1
    for item in V:
        mem = {}
        bad = False
        while True:
            if ans % item == 0:
                break
            if item % 2 == 0 and ans % item == item // 2:
                break
            if ans % item in mem:
                bad = True
                break
            mem[ans % item] = 1
            ans += inc
        if bad:
            ans = -1
            break
        inc = lcm(inc, ans)
    print(ans)
