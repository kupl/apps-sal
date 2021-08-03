def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = [mi() for i in range(n)]
p = 0
for i in range(n):
    s, d = a[i]
    if s > p:
        p = s
    else:
        q = p - s
        p = s + d * (q // d + 1)
print(p)
