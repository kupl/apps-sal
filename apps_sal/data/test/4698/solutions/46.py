a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = []
for i in range(c):
    d.append(list(map(int, input().split())))

for i in range(c):
    f = b.copy()
    p = d[i][0] - 1
    f[p] = d[i][1]
    print((sum(f)))
