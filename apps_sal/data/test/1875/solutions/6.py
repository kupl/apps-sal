def convex(p):
    p.sort(key=lambda x: (x.real, x.imag))
    p = p[0:1] + sorted(p[1:], key=lambda x: (x - p[0]).imag / abs(x - p[0]))
    j = 1
    for i in range(2, len(p)):
        while j > 1 and ((p[j] - p[j - 1]) * (p[i] - p[j]).conjugate()).imag > -(1e-8):
            j -= 1
        else:
            j += 1
            p[j] = p[i]
    return p[:j + 1]


def area(p):
    res = 0
    for i in range(2, len(p)):
        res += ((p[i] - p[i - 1]) * (p[i - 1] - p[0]).conjugate()).imag
    return res * 0.5


def tri(i, j, k):
    return abs(((w[i] - w[j]) * (w[i] - w[k]).conjugate()).imag) * 0.5


n = int(input())
p = [complex(*list(map(int, input().split()))) for i in range(n)]
w = convex(p)
n = len(w)
res = 0

for i in range(n):
    for j in range(i + 2, n):
        if i == 0 and j == n - 1:
            continue
        l, r = i + 1, j
        while l < r - 1:
            m = l + r >> 1
            if tri(i, j, m) > tri(i, j, m - 1):
                l = m
            else:
                r = m
        s1 = tri(i, j, l)
        l, r = j - n + 1, i
        while l < r - 1:
            m = l + r >> 1
            if tri(i, j, m) > tri(i, j, m - 1):
                l = m
            else:
                r = m
        s2 = tri(i, j, l)
        res = max(res, s1 + s2)

if n == 3:
    for i in p:
        if i in w:
            continue
        w.append(i)
        res = max(res, area(w))
        w.pop()

print(res)
