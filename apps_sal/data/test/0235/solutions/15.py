n = int(input())


def che(k):
    nn = n
    cnt = 0
    while nn:
        if nn <= k:
            cnt += nn
            break
        cnt += k
        nn -= k
        nn -= nn // 10
    return cnt << 1 >= n


(l, r) = (1, 1000000000000000000)
while l < r:
    mid = l + r >> 1
    if che(mid):
        r = mid
    else:
        l = mid + 1
print(r)
