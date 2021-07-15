n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))
se = list(set(s))
slov = dict()
for i in range(len(se)):
    slov[se[i]] = []
for i in range(len(s)):
    slov[s[i]].append([p[i], i + 1])
for i in se:
    slov[i].sort(reverse=True)
ans = [True] * (n + 1)
for i in se:
    ans[slov[i][0][1]] = False
ans1 = 0
for i in c:
    if ans[i]:
        ans1 += 1
print(ans1)
