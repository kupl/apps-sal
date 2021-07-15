def clock(a, b, c):
    u = b - a
    v = c - b
    return u.real * v.imag - u.imag * v.real < 0


n = int(input())
p = []
for i in range(n + 1):
    x, y = list(map(int, input().split()))
    p.append(complex(x, y))

cnt = 0
for i in range(1, n):
    if not clock(p[i - 1], p[i], p[i + 1]):
        cnt += 1

print(cnt)

