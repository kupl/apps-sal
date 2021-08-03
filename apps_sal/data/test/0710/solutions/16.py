n = int(input())
s = input()
res = 10**8
r = 'ACTG'


def f(a, b):
    u = 0
    for i in range(4):
        u += c(a[i], b[i])
    return u


def c(a, b):
    if a > b:
        return c(b, a)
    return min(ord(b) - ord(a), ord('Z') - ord(b) + ord(a) - ord('A') + 1)


for i in range(4, len(s) + 1):
    t = s[i - 4:i]
    res = min(res, f(t, r))
print(res)
