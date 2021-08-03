def valid(number_to_check, n, k):
    sum = 1
    sum = sum + (k) * (k - 1) // 2 - (k - number_to_check) * (k - number_to_check - 1) // 2
    if sum >= n:
        return True
    return False


def binary_serach(n, k):
    lo = 1
    hi = k
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if valid(mid, n, k):
            hi = mid
        else:
            lo = mid + 1
    if valid(lo, n, k):
        return lo
    else:
        return -1


n, k = map(int, input().split())
if n == 1:
    print(0)
elif n <= k:
    print(1)
else:
    print(binary_serach(int(n), int(k)))
