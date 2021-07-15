def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
p = [0] * n
for i in range(n):
    p[i] = [int(item) for item in input().split()]

wires = set()


for i in range(n):
    for j in range(i + 1, n):
        x0, y0 = p[i]
        x1, y1 = p[j]
        a = -(y1 - y0)
        b = (x1 - x0)
        c = x0 * (y1 - y0) - y0 * (x1 - x0)
        k = gcd(a, gcd(b, c))
        a //= k
        b //= k
        c //= k
        if a < 0:
            a *= -1
            b *= -1
            c *= -1
        wires.add((a, b, c))

wires = list(wires)

ans = 0
# print(wires)
for i in range(len(wires)):
    for j in range(i + 1, len(wires)):
        a1, b1, c1 = wires[i]
        a2, b2, c2 = wires[j]
        if b1 == 0:
            if b2 != 0:
                ans += 1
        elif b2 == 0:
            ans += 1
        else:
            if abs(a1 / b1 - a2 / b2) > 1e-7:
                ans += 1

print(ans)

