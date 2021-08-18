n, m = list(map(int, input().split()))
u = list(map(int, input().split()))
p = list(map(int, input().split()))
for i in range(1, n):
    u[i] -= u[0]
h = u[0]
u[0] = 0


def gsd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gsd(b, a % b)


for i in range(1, n):
    u[i] = gsd(u[i], u[i - 1])
for i in range(m):
    if u[-1] % p[i] == 0:
        print("YES")
        print(h, i + 1)
        return
print("NO")
