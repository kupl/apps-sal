H, W = map(int, input().split())
p = []
for i in range(H):
    p.append(list(input()))

l = u = +100500
b = r = -100500
for i in range(H):
    for j in range(W):
        if p[i][j] == "X":
            l = min(l, j)
            r = max(r, j)

            u = min(u, i)
            b = max(b, i)


for i in range(u, b + 1):
    for j in range(l, r + 1):
        if p[i][j] == ".":
            print("NO")
            return

print("YES")
