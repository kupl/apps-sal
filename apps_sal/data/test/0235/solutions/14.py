n = int(input())


def check(k):
    a, b = 0, 0
    i = n
    while i > 0:
        t = min(k, i)
        a += t
        i -= t

        t = i // 10
        b += t
        i -= t
    # dbvar(k, a, b)
    return a >= b


left = 1
right = n
while right - left > 1:
    m = (left + right) // 2
    if check(m):
        right = m
    else:
        left = m
print(left if check(left) else right)
