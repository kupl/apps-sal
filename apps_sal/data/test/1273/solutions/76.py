n = int(input())
a = [set() for i in range(n)]
e = []
for i in range(n - 1):
    b, c = map(int, input().split())
    b -= 1
    c -= 1
    a[b].add(c)
    a[c].add(b)
    e.append(c)

col = [0 for i in range(n)]
visited = [False for i in range(n)]
visited[0] = True
v = [0]

while v:
    d = v.pop(0)
    k = 1
    for i in a[d]:
        if visited[i] == False:
            if col[d] == k:
                k += 1
            col[i] = k
            visited[i] = True
            v.append(i)
            k += 1

print(max(col))
for i in e:
    print(col[i])
