n,m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
b = [[] for _ in range(8)]
c = []
for i in range(n):
    x,y,z = a[i][0],a[i][1],a[i][2]
    b[0].append(x+y+z)
    b[1].append(x+y-z)
    b[2].append(x-y+z)
    b[3].append(x-y-z)
    b[4].append(-x+y+z)
    b[5].append(-x+y-z)
    b[6].append(-x-y+z)
    b[7].append(-x-y-z)
for i in range(8):
    b[i].sort()
    b[i].reverse()
for i in range(8):
    c.append(sum(b[i][:m]))
print((max(c)))

