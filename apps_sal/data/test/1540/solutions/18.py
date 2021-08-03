n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
l = [[0] * m] * n

for i in range(n):
    l[i] = list(map(int, input().split()))

t = [[0] * 2] * k
e = [0] * n
c = [0] * m

for i in range(k):
    t0, t1 = map(int, input().split())
    e[t0 - 1] -= 1
    c[t1 - 1] += 1

p = [""] * n
for i in range(n):
    for j in range(m):
        e[i] = e[i] + c[j] * l[i][j]
    p[i] = str(e[i])

print(" ".join(p))
