MOD = 1000000007
n, k = list(map(int, input().split()))
ch = [set() for _ in range(n + 1)]
for _2 in range(n - 1):
    u, v, x = list(map(int, input().split()))
    if x == 0:
        ch[u].add(v)
        ch[v].add(u)
res = 0
root = [True] * (n + 1)
for i in range(1, n + 1):
    if root[i]:
        cur = 1
        stack = [i]
        while stack:
            u = stack.pop()
            for v in ch[u]:
                ch[v].remove(u)
                cur += 1
                root[v] = False
                stack.append(v)
        res = (res + pow(cur, k)) % MOD
res = (MOD + pow(n, k) - res) % MOD
print(res)

