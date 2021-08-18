n = int(input())

if n <= 10:
    print("1")
    return


def check(k):
    out = 0
    cur = n
    while cur != 0:
        tmp = min(cur, k)
        cur -= tmp
        out += tmp
        if cur >= 10:
            cur -= cur // 10
    return out


l = 0
r = 10 ** 18 + 1
k = (l + r) // 2
while r - l > 1:
    if 2 * check(k) >= n:
        r = k
    else:
        l = k
    k = (l + r) // 2

print(k + 1)
