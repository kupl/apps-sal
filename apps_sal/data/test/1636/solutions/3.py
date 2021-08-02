n = int(input())
MAX = 100000
coord = [list() for i in range(2 * MAX + 1)]
for i in range(n):
    x, y = map(int, input().split())
    coord[y - x - MAX].append((x, y))
w = list(map(int, input().split()))
for i in range(2 * MAX + 1):
    coord[i].sort()
ans = [(0, 0) for i in range(n)]
possible = True
last_x = [-1] * (MAX + 1)
last_y = [-1] * (MAX + 1)
for i in range(n):
    if len(coord[w[i] - MAX]) > 0:
        x = coord[w[i] - MAX][0][0]
        y = coord[w[i] - MAX][0][1]
        if last_x[y] == x - 1 and last_y[x] == y - 1:
            last_x[y] += 1
            last_y[x] += 1
            ans[i] = x, y
            coord[w[i] - MAX].pop(0)
        else:
            possible = False
            break
    else:
        possible = False
        break
if possible:
    print("YES")
    print("\n".join([" ".join(map(str, coords)) for coords in ans]))
else:
    print("NO")
