n = int(input())
# a,b=map(int,input().split())
al = list(map(int, input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
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
