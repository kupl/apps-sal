n, m = list(map(int, input().split()))
c = 0
for i in range(n):
    appts = list(map(int, input().split()))
    for j in range(m):
        x = appts[2 * j]
        y = appts[2 * j + 1]
        c += (1 if (x > 0 or y > 0) else 0)

print(c)
