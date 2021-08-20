def aaa(a, b):
    return abs(a // 3 * b - (a // 3 + 1) * b)


def bbb(a, b):
    ret = 1000 * 100
    for x in range(1, a):
        xx = a - x
        i = x * b
        j = xx * (b // 2)
        k = xx * (b // 2 + b % 2)
        tmp = max(abs(i - j), abs(j - k), abs(k - i))
        ret = min(ret, tmp)
    return ret


(H, W) = list(map(int, input().split()))
if H % 3 == 0 or W % 3 == 0:
    print(0)
else:
    a = aaa(H, W)
    b = aaa(W, H)
    c = bbb(H, W)
    d = bbb(W, H)
    print(min(a, b, c, d))
