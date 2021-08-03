n, k = map(int, input().split())

a = list(map(int, input().split()))

c = [0, 0, 0, 0]

for t in a:
    c[0] += t // 4
    if t % 4:
        c[t % 4] += 1

c[0] += c[3]
c[3] = 0

if c[0] > n:
    c[2] += 2 * (c[0] - n)
    c[0] = n

t = min(n - c[0], c[1], c[2])
c[0] += t
c[1] -= t
c[2] -= t

t = min(n - c[0], (c[1] + 1) // 2)
c[0] += t
c[1] -= min(c[1], t * 2)

t = min(n - c[0], c[2])
c[0] += t
c[2] -= min(c[2], t + t // 2)

c[2] += c[1]
c[1] = 0

print("YES" if c[2] <= 2 * n else "NO")
