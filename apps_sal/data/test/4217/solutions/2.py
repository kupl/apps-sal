import collections
n,m = list(map(int, input().split()))
l = [list(map(int, input().split())) for l in range(n)]
tmp = []

for i in range(n):
    for a in range(l[i][0]):
        tmp.append(l[i][a + 1])

c = collections.Counter(tmp)

ans = []
for x in list(c.items()):
    if x[1] == n:
        ans.append(x[0])
print((len(ans)))

