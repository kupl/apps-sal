def is_good(mid, key):
    res = 0
    for a in A:
        res += (a + mid - 1) // mid
    return res - N <= key


def binary_search(bad, good, key):
    while good - bad > 1:
        mid = (bad + good) // 2
        if is_good(mid, key):
            good = mid
        else:
            bad = mid
    return good


N, K, *A = list(map(int, open(0).read().split()))
print((binary_search(0, 1_000_000_000, K)))

