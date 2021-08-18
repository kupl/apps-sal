n = int(input())

c = [[0] + list(map(int, input().split())) for _ in range(3)]

e = [set() for u in range(n + 1)]

for i in range(n - 1):
    u, v = list(map(int, input().split()))
    e[u].add(v)
    e[v].add(u)

for i in range(1, n + 1):
    if len(e[i]) > 2:
        print(-1)
        return

for i in range(1, n + 1):
    if len(e[i]) == 1:
        S = i
        break

s = [S, next(iter(e[S]))]

for i in range(n - 2):
    u = s[-1]
    for v in e[u]:
        if v == s[-2]:
            continue
        s.append(v)
        break

ans, ans_d = 10 ** 100, []
d = [0 for _ in range(n + 1)]

for i in range(3):
    for j in range(3):
        if i != j:
            d[s[0]] = i + 1
            d[s[1]] = j + 1
            for k in range(2, n):
                d[s[k]] = 6 - (d[s[k - 1]] + d[s[k - 2]])
            w = sum([c[d[u] - 1][u] for u in range(1, n + 1)])
            if w < ans:
                ans = w
                ans_d = d[::]

print(ans)
print(*ans_d[1:])
