n = int(input())
red, blue = [], []
ans = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    red.append((max(a, b), a, b))
for _ in range(n):
    c, d = list(map(int, input().split()))
    blue.append((min(c, d), c, d))
red.sort(key=lambda x: x[0], reverse=True)
blue.sort(key=lambda x: x[0])
for i in range(n):
    _, xb, yb = blue[i]
    for j in range(n):
        if red[j]:
            _, xr, yr = red[j]
            if xb > xr and yb > yr:
                red[j] = False
                ans += 1
                break
print(ans)

