n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = []
c = []
for i in range(n):
    b.append(a[i][0] + a[i][1])
    c.append(a[i][0] - a[i][1])
maxbc = [max(b) - min(b), max(c) - min(c)]
print(max(maxbc))
