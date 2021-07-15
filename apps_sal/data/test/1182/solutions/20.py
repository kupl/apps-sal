r, c, n, k = input().split()
r, c, n, k = int(r), int(c), int(n), int(k)

violas = []

for _ in range(n):
    x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    violas.append((y,x))

def count_violas(x1, y1, x2, y2):
    nonlocal violas
    s = 0
    for x, y in violas:
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            s += 1
    return s

ans = 0
for x1 in range(c):
    for y1 in range(r):
        for x2 in range(x1, c):
            for y2 in range(y1, r):
                if count_violas(x1, y1, x2, y2) >= k:
                    ans += 1

print(ans)
