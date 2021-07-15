n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
l = [[] for i in range(n)]
ab.sort()
for i in range(m):
    x = ab[i]
    l[x[0]-1].append(x[1]-1)
    l[x[1]-1].append(x[0]-1)
for i in l[0]:
    if n-1 in l[i]:
        print("POSSIBLE")
        return
print("IMPOSSIBLE")
