n = int(input())


def gcd(x, y):
    while y > 0:
        (x, y) = (y, x % y)
    return x


poles = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    poles.append((x, y))
lines = set()
for i in range(len(poles) - 1):
    for j in range(i + 1, len(poles)):
        p1 = poles[i]
        p2 = poles[j]
        a = p1[1] - p2[1]
        b = -p1[0] + p2[0]
        abg = gcd(abs(a), abs(b))
        if abg > 0:
            a //= abg
            b //= abg
        if a < 0:
            a = -a
            b = -b
        if a == 0:
            b = 1
        if b == 0:
            a = 1
        c = -a * p1[0] - b * p1[1]
        lines.add((a, b, c))
cnt = 0
for (i, line1) in enumerate(lines):
    for (j, line2) in enumerate(lines):
        if i >= j:
            continue
        if line1[:2] != line2[:2]:
            cnt += 1
print(cnt)
