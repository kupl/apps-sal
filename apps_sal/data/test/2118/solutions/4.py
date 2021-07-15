n, k = [int(i) for i in input().split()]
if k % 2 == 0 or k >= 2 * n:
    print(-1)
    return
last = n
a = [0] * n
def ans(c, l, r):
    nonlocal last
    if c == 1:
        i = r - 1
        while i >= l:
            a[i] = last
            last -= 1
            i -= 1
        return
    m = (l + r) // 2
    ans(c // 2 - int((c // 2) % 2 == 0), l, m)
    ans(c // 2 + int((c // 2) % 2 == 0), m, r)
ans(k, 0, n)
print(*a)

