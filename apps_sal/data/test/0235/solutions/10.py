n = int(input())


def eat(n, k):
    first = 0
    old = n
    while n > 0:
        if n > k:
            n -= k
            first += k
        else:
            first += n
            n = 0
        n -= n // 10
    if 2 * first >= old:
        return True
    return False


r = n + 1
l = 1
while l + 1 < r:
    m = l + (r - l - 1) // 2
    if eat(n, m):
        r = m + 1
    else:
        l = m + 1
print(l)
