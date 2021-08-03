from sys import stdin
i = [[int(y) for y in x.rstrip().split()] for x in stdin.readlines()]
k = i[0][1]
days = i[1]
remaining = 0
for i, x in enumerate(days):
    k -= min(8, x + remaining)
    remaining = x + remaining - min(8, x + remaining)
    if k <= 0:
        print(i + 1)
        break
else:
    print(-1)
