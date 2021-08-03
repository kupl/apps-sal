n, m = map(int, input().split())
ll = []
for i in range(n):
    l = list(map(int, input().split()))
    ll.append(l)

ll.sort()

t = 0
cst = 0
i = 0
while t < m:
    t += ll[i][1]
    cst += ll[i][0] * ll[i][1]
    if t > m:
        cst -= ll[i][0] * (t - m)
    i += 1
print(cst)
