n, m = list(map(int, input().split()))
light = [list(map(int, input().split())) for _ in range(m)]
lighton = list(map(int, input().split()))
swicth = []

for i in range(2**n):
    a = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            a[j] = 1
    swicth.append(a)

ans = 0

for x in swicth:
    for y in range(m):
        b = light[y][1:]
        total = 0
        for z in b:
            total += x[z - 1]
        if total % 2 != lighton[y]:
            break
    else:
        ans += 1

print(ans)
