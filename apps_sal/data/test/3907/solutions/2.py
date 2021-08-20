def Fun(n):
    if n % 2:
        return n * (n - 1) // 2 + 1
    return n * n // 2


(n, m) = list(map(int, input().split()))
q = [0] * m
w = [0] * m
for i in range(m):
    (q[i], w[i]) = [int(x) for x in input().split()]
w.sort(reverse=True)
s = 0
v = 0
for i in range(m):
    if Fun(i + 1) > n:
        break
    s += w[i]
print(s)
