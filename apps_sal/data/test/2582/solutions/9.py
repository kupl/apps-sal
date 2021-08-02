n = int(input())
a = list(map(int, input().split()))
if a == [i + 1 for i in range(n)]:
    print(0)
    return
if a == [i + 1 for i in range(n)][::-1]:
    print(0)
    return
p = [0] * (n + 1)
p[0] = -1
for i in range(n):
    p[a[i]] = i
num = 2**(n - 1).bit_length()


def segfunc(x, y):
    if a[x] < a[y]:
        return y
    else:
        return x


seg = [0] * (2 * num - 1)
for i in range(n):
    seg[i + num - 1] = i
for i in range(num - 2, -1, -1):
    seg[i] = segfunc(seg[2 * i + 1], seg[2 * i + 2])


def update(i, x):
    i += num - 1
    seg[i] = x
    while i:
        i = (i - 1) // 2
        seg[i] = segfunc(seg[i * 2 + 1], seg[i * 2 + 2])


def query(l, r):
    l += num - 1
    r += num - 2
    if l == r:
        return seg[l]
    s = seg[l]
    l += 1
    while r - l > 1:
        if ~l % 2:
            s = segfunc(seg[l], s)
        if r % 2:
            s = segfunc(seg[r], s)
            r -= 1
        l //= 2
        r = (r - 1) // 2
    if l == r:
        return segfunc(s, seg[l])
    return segfunc(s, segfunc(seg[l], seg[r]))


def f(l, r):
    if r - l < 2:
        return 0
    maxi = query(l, r + 1)
    ma = a[maxi]
    ans = f(l, maxi - 1) + f(maxi + 1, r)
    if maxi - l < r - maxi:
        for i in range(l, maxi):
            if maxi < p[ma - a[i]] <= r:
                ans += 1
    else:
        for i in range(maxi + 1, r + 1):
            if l <= p[ma - a[i]] < maxi:
                ans += 1
    return ans


print(f(0, n - 1))
