
def calc(k):
    if k is 0:
        return 0
    num, ret, pre = len(str(k)), 0, 0
    for i in range(1, num):
        cnt = pow(10, i - 1) * 9
        ret += pre * cnt + i * (1 + cnt) * cnt // 2
        pre += i * cnt
    extra = k - pow(10, num - 1) + 1
    ret += pre * extra
    ret += num * (1 + extra) * extra // 2
    return int(ret)


def ds(k):
    num, _sum = 1, 0
    while _sum + num * pow(10, num - 1) * 9 < k:
        _sum += num * pow(10, num - 1) * 9
        num += 1
    k -= _sum
    val = pow(10, num - 1) + k // num
    if k % num is 0:
        return (val - 1) % 10
    k = num - (k % num)
    for i in range(k):
        val = val // 10
    return val % 10


def solve(k):
    l, r, ans = 0, 1e9 + 7, 0
    while l <= r:
        mid = int((l + r) // 2)
        if calc(mid) >= k:
            ans, r = mid, mid - 1
        else:
            l = mid + 1
    k = k - calc(ans - 1)
    return ds(k)


q = int(input())

for i in range(q):
    k = int(input())
    print(solve(k))
