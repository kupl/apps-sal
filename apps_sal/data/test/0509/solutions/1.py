def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
a = [ii() for i in range(n)]
ans = 0
for i in range(2 ** n):
    s = 0
    for b in range(n):
        if i >> b & 1:
            s += a[b]
        else:
            s -= a[b]
    if s % 360 == 0:
        ans = 1
        break
print('YES' if ans else 'NO')
