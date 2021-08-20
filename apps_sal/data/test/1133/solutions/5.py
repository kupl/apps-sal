n = int(input())
a = [input() for i in range(n)]
alp = 'qwertyuiopasdfghjklzxcvbnm'
ans = 0
for i in range(26):
    for j in range(i + 1, 26):
        (c1, c2) = (alp[i], alp[j])
        cur = 0
        for s in a:
            if set(s) in ({c1, c2}, {c1}, {c2}):
                cur += len(s)
        ans = max(ans, cur)
print(ans)
