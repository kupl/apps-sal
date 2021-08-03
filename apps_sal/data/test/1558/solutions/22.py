import operator
n, r, avg = list(map(int, input().split()))
x, y = 0, 0
s = 0
l = []
for i in range(n):
    x, y = list(map(int, input().split()))
    l.append([x, y])
    s += x
l.sort(key=operator.itemgetter(1))
s = n * avg - s
ans, i = 0, 0
while s > 0 and i < n:
    ans += min(s, r - l[i][0]) * l[i][1]
    s -= min(s, r - l[i][0])
    i += 1
print(ans)
