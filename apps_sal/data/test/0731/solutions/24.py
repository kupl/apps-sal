w, m, k = map(int, input().split())


def size(a):
    return len(str(a))


def how_many(m, n):
    len1 = size(m)
    len2 = size(n)
    if len1 == len2:
        return (n - m + 1) * len1
    else:
        cnt = 0
        for len in range(len1, len2 + 1):
            if len == len1:
                cnt += (pow(10, len1) - m) * len
            elif len == len2:
                cnt += (n - pow(10, len2 - 1)) * len
            else:
                cnt += (pow(10, len) - pow(10, len - 1)) * len
        return cnt + len2


def check(n):
    return how_many(m, n) * k <= w


l = m
r = 10 ** 18
while (r - l > 1):
    n = l + (r - l) // 2
    if check(n):
        l = n
    else:
        r = n
if l != m:
    print(l - m + 1)
else:
    print(int(check(m)))
