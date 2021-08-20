n = int(input())
l = [[] for i in range(4)]
for i in range(n):
    (x, y) = list(map(int, input().split()))
    l[0].append(x + y)
    l[1].append(x - y)
    l[2].append(-x + y)
    l[3].append(-x - y)
for i in range(4):
    l[i].sort()
ans = 0
for i in range(4):
    ans = max(ans, l[i][-1] - l[i][0])
print(ans)
