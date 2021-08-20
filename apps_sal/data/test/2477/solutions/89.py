(n, k) = list(map(int, input().split()))
a_l = [int(x) for x in input().split()]
left = 0
right = max(a_l)


def cut(len):
    ret = 0
    for i in range(n):
        if a_l[i] % len == 0:
            ret += a_l[i] // len - 1
        else:
            ret += a_l[i] // len
    return ret


while right - left > 1:
    _q = (left + right) // 2
    _ret = cut(_q)
    if k >= _ret:
        right = _q
    else:
        left = _q
print(right)
