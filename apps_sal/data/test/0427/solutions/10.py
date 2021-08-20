(cnt1, cnt2, x, y) = map(int, input().split())
upper_limit = (cnt1 + cnt2) * (x * y) // (x * y - x - y + 1)


def bin_search(low, high):
    if low >= high - 1:
        return high
    mid = (low + high) // 2
    best_way = max(0, cnt1 - mid // y + mid // (x * y)) + max(0, cnt2 - mid // x + mid // (x * y))
    leftovers = mid - mid // x - mid // y + mid // (x * y)
    if best_way <= leftovers:
        return bin_search(low, mid)
    return bin_search(mid, high)


print(bin_search(1, upper_limit + 10))
