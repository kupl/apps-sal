from collections import Counter
(n, k) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
MOD = 998244353
lst1 = [[] for _ in range(n)]
lst2 = [[] for _ in range(n)]
g1 = [-1] * n
g2 = [-1] * n
for i in range(n - 1):
    for j in range(i + 1, n):
        jdg1 = True
        jdg2 = True
        for l in range(n):
            if a[i][l] + a[j][l] > k:
                jdg1 = False
            if a[l][i] + a[l][j] > k:
                jdg2 = False
            if not jdg1 and (not jdg2):
                break
        if jdg1:
            lst1[i].append(j)
            lst1[j].append(i)
            g1[i] = 0
            g1[j] = 0
        if jdg2:
            lst2[i].append(j)
            lst2[j].append(i)
            g2[i] = 0
            g2[j] = 0


def calc(lst, g):
    cnt = 1
    for i in range(n):
        if g[i] != 0:
            continue
        temp = [i]
        g[i] = cnt
        while temp:
            p = temp.pop()
            for ip in lst[p]:
                if g[ip] != 0:
                    continue
                g[ip] = cnt
                temp.append(ip)
        cnt += 1
    return g


g1 = calc(lst1, g1)
cnt1 = Counter(g1)
g2 = calc(lst2, g2)
cnt2 = Counter(g2)
ans = 1
for (i, v) in cnt1.items():
    if i == -1:
        continue
    for j in range(1, v + 1):
        ans *= j % MOD
    ans %= MOD
for (i, v) in cnt2.items():
    if i == -1:
        continue
    for j in range(1, v + 1):
        ans *= j % MOD
    ans %= MOD
print(ans)
