n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    inp = list(map(int, input().split()))
    c_, a_ = inp[0], inp[1:]
    c.append(c_)
    a.append(a_)

ans = float('inf')
for bit in range(1 << n):
    cost = 0
    skill = [0] * m
    for i in range(n):
        if bit & 1 << i:
            cost += c[i]
            for j in range(m):
                skill[j] += a[i][j]
    if min(skill) >= x:
        ans = min(ans, cost)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
