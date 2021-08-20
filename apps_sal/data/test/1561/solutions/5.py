(n, m, k) = list(map(int, input().split()))
f = [[x == '.' for x in input()] for _ in range(n)]
if k == 1:
    print(sum((sum(x) for x in f)))
    quit()
r = 0
for y in range(n):
    (b, e) = (0, 1)
    for x in range(m):
        if f[y][x]:
            e += 1
        else:
            r += max(0, e - b - k)
            (b, e) = (x, x + 1)
    r += max(0, e - b - k)
for x in range(m):
    (b, e) = (0, 1)
    for y in range(n):
        if f[y][x]:
            e += 1
        else:
            r += max(0, e - b - k)
            (b, e) = (x, x + 1)
    r += max(0, e - b - k)
print(r)
