3


def readn():
    return map(int, input().split())


(n, m, a) = readn()
n = min(n, m)
m = n
b = sorted(readn())[-n:]
p = sorted(readn())
r = 0
while r < n:
    t = (r + 1 + n) // 2
    a1 = sum([max(0, p[i] - b[m + i - t]) for i in range(t)])
    if a1 <= a:
        r = t
    else:
        n = t - 1
print(r, max(0, sum(p[:r]) - a))
