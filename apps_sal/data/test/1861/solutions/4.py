(n, k) = [int(s) for s in input().split()]
l = [input().strip() for i in range(n)]
s = set(l)
comp = {'ST': 'E', 'TS': 'E', 'SE': 'T', 'ES': 'T', 'ET': 'S', 'TE': 'S'}
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        s1 = ''
        for w in range(k):
            if l[i][w] == l[j][w]:
                s1 += l[i][w]
            else:
                s1 += comp[l[i][w] + l[j][w]]
        if s1 in s:
            ans += 1
print(ans // 3)
