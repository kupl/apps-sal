N = 1000
dis = set([])
n, m = list(map(int, input().split(' ')))
f = False
for i in range(n):
    s = input()
    dist = s.index('S') - s.index('G')
    # print(dist)
    if dist < 0:
        f = True
        break
    if dist not in dis:
        dis.add(dist)
if f:
    print(-1)
else:
    print(len(dis))
