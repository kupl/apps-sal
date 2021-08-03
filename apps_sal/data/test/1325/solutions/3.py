def distchar(a, b):
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    if a > b:
        a, b = b, a
    return min(b - a, a + 26 - b)


def dist(i, p, n):
    if p >= i:
        sign = 1
    else:
        sign = -1
    return sign * min(abs(p - i), abs((n - 1 - i) - p))


[n, p] = [int(s) for s in input().split()]
s = input().strip()

p = p - 1  # change to 0-based


# print(s)

count1 = 0
d = [0 for i in range(n)]
for i in range(n // 2):
    di = distchar(s[i], s[n - 1 - i])
    if di > 0:
        d[i], d[n - 1 - i] = di, di
        count1 += di

if p > n // 2:
    p = n - 1 - p

i1 = 0
while i1 < p and d[i1] == 0:
    i1 += 1
i2 = (n - 1) // 2
while i2 > p and d[i2] == 0:
    i2 -= 1
d1 = dist(i1, p, n)
d2 = dist(i2, p, n)
if d1 * d2 > 0:
    count = count1 + max(abs(d1), abs(d2))
else:
    count = count1 + 2 * min(abs(d1), abs(d2)) + max(abs(d1), abs(d2))

print(count)


##        print(' '.join(map(str,A[i])))
