def count(x):
    result = 0
    while x:
        result += x // 5
        x //= 5
    return result


def find(n):
    (l, r) = (0, 25 * n)
    while l + 1 < r:
        m = l + r >> 1
        if count(m) < n:
            l = m
        else:
            r = m
    return r


m = int(input())
(l, r) = (find(m), find(m + 1))
print(r - l)
print(*list(range(l, r)))
