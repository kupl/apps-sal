def getfather(x):
    if x == fa[x]:
        return x
    fa[x] = getfather(fa[x])
    return fa[x]


n = int(input())
s = list(input())
t = list(input())
fa = [_ for _ in range(26)]
ans = []
tot = 0
for i in range(n):
    x = ord(s[i]) - 97
    y = ord(t[i]) - 97
    fx = getfather(x)
    fy = getfather(y)
    if fx != fy:
        fa[fx] = fy
        tot += 1
        ans.append((chr(x + 97), chr(y + 97)))
print(tot)
for i in ans:
    print(i[0] + ' ' + i[1])
