n, m = map(int, input().split())
color = list(map(int, input().split()))

x = list(zip(*[list(map(int, input().split())) for i in range(m)]))
y = x[1]
x = x[0]

ans = dict()

for i in color:
    if i not in ans:
        ans[i] = set()

for i in range(m):
    if color[x[i] - 1] != color[y[i] - 1]:
        ans[color[x[i] - 1]].add(color[y[i] - 1])
        ans[color[y[i] - 1]].add(color[x[i] - 1])

for i in ans:
    Max = i
    break

MaxLen = len(ans[Max])
for i in ans:
    LAns = len(ans[i])
    if (MaxLen < LAns) or ((MaxLen == LAns) and (Max > i)):
        Max = i
        MaxLen = LAns

print(Max)
