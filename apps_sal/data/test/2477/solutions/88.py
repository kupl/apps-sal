def is_good(mid, key):
    return sum(((a + mid - 1) // mid for a in A)) - N <= key


def binary_search(bad, good, key):
    while good - bad > 1:
        mid = (bad + good) // 2
        if is_good(mid, key):
            good = mid
        else:
            bad = mid
    return good


(N, K, *A) = list(map(int, open(0).read().split()))
print(binary_search(0, 1000000000, K))
