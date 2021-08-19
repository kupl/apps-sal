(n, s) = map(int, input().split())
mass = [0] * n
for i in range(n - 1):
    (a1, b1) = map(int, input().split())
    a1 -= 1
    b1 -= 1
    mass[a1] += 1
    mass[b1] += 1
cnt = 0
for i in mass:
    cnt += i == 1
print(2 * s / cnt)
