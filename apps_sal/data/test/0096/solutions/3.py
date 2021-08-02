import sys


def cnt(y, n):
    # print("in count")
    # print(y)
    if y <= 1:
        return n
    if y > n:
        return 0
    if y % 2 == 1:
        return 1 + cnt(2 * y, n)
    c = 0
    p = 1
    while p * y <= n:
        mx = min(n, p * y + 2 * p - 1)
        c += mx - p * y + 1
        p *= 2
    return c


n, k = input().split()
n, k = int(n), int(k)

if k == 1:
    print(n)
    return

l, h = 1, n // 2
while l < h:
    m = (l + h) // 2
    #print("l = " + str(l))
    #print("h = " + str(h))
    #print("m = " + str(m))
    #print("cnt = " + str(cnt(m, n)))

    if cnt(2 * m, n) < k:
        h = m
    else:
        l = m + 1
mx_even = 2 * l - 2

l, h = 1, n // 2
while l < h:
    m = (l + h) // 2
    #print("l = " + str(l))
    #print("h = " + str(h))
    #print("m = " + str(m))
    #print("cnt = " + str(cnt(m, n)))

    if cnt(2 * m + 1, n) < k:
        h = m
    else:
        l = m + 1
mx_odd = 2 * l - 1
#assert(cnt(mx_odd, n) >= k)
#assert(cnt(mx_even, n) >= k)

mx_heur = -1
i = 0
while i < 20 and n - i > 0:
    if cnt(n - i, n) >= k:
        mx_heur = n - i
        break
    i += 1

print(max(mx_even, max(mx_odd, mx_heur)))
