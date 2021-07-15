input()
s = input()

def min_d(a, b):
    a, b = ord(a), ord(b)
    a, b = a - b, b - a
    if a < 0:
        a += 26
    if b < 0:
        b += 26
    return min(a, b)

ans = 999
for a, b, c, d in zip(s, s[1:], s[2:], s[3:]):
    ans = min(ans, sum(min_d(x, y) for x, y in ((a, 'A'), (b, 'C'), (c, 'T'), (d, 'G'))))

print(ans)

