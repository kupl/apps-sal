n, m, k, x, y = list(map(int, input().split()))

if n == 1:
    cnt = k // m
    k %= m
else:
    cnt = k // (2 * m * (n - 1))
    k %= 2 * m * (n - 1)

q = [[2 * cnt] * m for i in range(n)]
q[0] = [cnt] * m
q[-1] = [cnt] * m

i = 0
j = 0
d = 1
while k > 0:
    q[i][j] += 1

    k -= 1
    j += 1
    if d == 1:
        i += j // m
        j %= m
    elif d == -1:
        i -= j // m
        j %= m

    if i == n:
        i = n - 2
        d = -1

gmin = 10**18
gmax = 0
for line in q:
    gmin = min(gmin, min(line))
    gmax = max(gmax, max(line))
print(gmax, gmin, q[x - 1][y - 1])
