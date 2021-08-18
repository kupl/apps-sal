n, m = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]
summ = sum(l)
result = 0


def find(x):
    # xét nếu uống trong x ngày kịp làm
    # thứ tự uống trong mỗi ngày ưu tiên cốc lớn trước . ex : với x = 2 : a1x1 > a1x2 > a2x1 >a2x2 >...
    s = 0
    pos_count = 0
    day_count = 0

    for i in l:
        s += max(0, i - pos_count)
        day_count += 1
        if day_count == x:
            day_count = 0
            pos_count += 1

    if s < m:
        return 0
    else:
        return x


def binary_search(lf, r):
    nonlocal result
    mid = int((lf + r) / 2)

    rs = find(mid)

    if lf == r:
        result = rs
    elif lf == r - 1:
        if rs:
            result = rs
        else:
            binary_search(r, r)
    else:
        if rs:
            binary_search(lf, mid)
        else:
            binary_search(mid, r)


if summ < m:
    print('-1')
elif summ == m:
    print(n)
# elif summ - sum(range(n)) == m:
#     print('1')
else:
    l = sorted(l, reverse=True)
    binary_search(1, n)
    print(result)
