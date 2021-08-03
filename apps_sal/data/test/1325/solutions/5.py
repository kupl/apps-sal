def dc(c, d):
    x, y = ord(c) - ord('a'), ord(d) - ord('a')
    return min(abs(x - y), 26 - max(x, y) + min(x, y))


def ds(s1, s2):
    r = 0
    a, b = 10 ** 5, -1
    for i in range(len(s1)):
        c, d = s1[i], s2[i]
        r += dc(c, d)
        if c != d:
            a = min(a, i)
            b = max(b, i)
    return a, b, r


n, p = list(map(int, input().split()))
s = input()
p -= 1
m = n // 2
y = m + (1 if n % 2 else 0)
s1, s2 = s[:m], s[y:][::-1]
a, b, r = ds(s1, s2)
#print(s1, s2, a, b, r)
d1 = min(abs(p - a), abs(p - b)) + abs(a - b)
d2 = min(abs(p - y - m + 1 + a), abs(p - y - m + 1 + b)) + abs(a - b)
#print(d1, d2)
if r == 0:
    print(0)
else:
    print(min(d1, d2) + r)
