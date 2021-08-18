n = int(input())
al = list(map(int, input().split()))
d = [0]
d = d + al
d.append(0)
totald = 0
for i in range(1, n + 2):
    totald += abs(d[i] - d[i - 1])

for i in range(1, n + 1):
    minus = abs(d[i] - d[i - 1]) + abs(d[i + 1] - d[i])
    add = abs(d[i + 1] - d[i - 1])
    print((totald - minus + add))
