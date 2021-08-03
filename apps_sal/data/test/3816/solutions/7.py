p = list(map(int, input().split()))
l = p.pop()
n = (l + 1) * (l + 2) * (l + 3) // 6
s = sum(p)
for q in p:
    t = 2 * q - s
    for d in range(l + 1):
        k = min(t + d, l - d) + 1
        if k > 0:
            n -= k * k + k >> 1
print(n)
