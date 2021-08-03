n, m = map(int, input().split())
p = list(map(int, input().split()))
for _ in range(m):
    l, r, x = map(int, input().split())
    y = p[x - 1]
    c = 0
    for z in range(l - 1, r):
        if p[z] < y:
            c += 1
    print("Yes" if c == x - l else "No")
