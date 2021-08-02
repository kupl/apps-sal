def cnt_zeroes(n):
    p5 = 1
    i = 0
    while 5 * p5 <= n:
        p5 *= 5
        i += 1
    ans = 0
    all_cnt = 0
    while p5 > 1:
        ans += i * (n // p5 - all_cnt)
        all_cnt += (n // p5 - all_cnt)
        p5 //= 5
        i -= 1
    return ans


def bin_search(n):
    l = 1
    r = 1000000
    while r - l > 1:
        m = (l + r) // 2
        if cnt_zeroes(m) < n:
            l = m + 1
        else:
            r = m
    if cnt_zeroes(l) == n:
        return l
    else:
        return r


n = int(input())
f = bin_search(n)
if cnt_zeroes(f) == n:
    print(5)
    for x in range(f, f + 5):
        print(x, end=' ')
    print()
else:
    print(0)
