k = int(input())
a, c = [], {}
for i in range(k):
    a.append([])
    n, a[i], s = int(input()), [], 0
    for j in input().split():
        a[i] += [-int(j)]
        s += int(j)
    for j in range(n):
        a[i][j] += s
        h = c.get(a[i][j])
        if h != None and h[0] != i + 1:
            print("YES")
            print(h[0], h[1])
            print(1 + i, 1 + j)
            quit()
        c[a[i][j]] = [i + 1, j + 1]
print("NO")
