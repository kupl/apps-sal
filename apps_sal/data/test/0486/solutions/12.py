def mp():
    return map(int, input().split())


def f(x):
    r = 1
    for i in str(x):
        r *= int(i)
    return r


n = int(input())
r = f(n)
l = len(str(n))
for i in range(l):
    s = str(n)
    k = int(s[:i] + str(max(0, int(s[i]) - 1)) + '9' * (l - i - 1))
    r = max(r, f(k))
print(r)
