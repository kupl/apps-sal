m, n, k, t = list(map(int, input().split()))

soldiers = list(map(int, input().split()))
traps = []
for _ in range(k):
    l, r, d = list(map(int, input().split()))
    traps.append((l, r, d))

soldiers.sort(reverse=True)
traps.sort()


def cost(count):
    agil = soldiers[count - 1] if count > 0 else 10**6
    current_begin = 0
    current_end = -1
    inter_cost = 0

    for l, r, d in traps:
        if d <= agil:
            continue
        if l > current_end:
            inter_cost += 2 * (current_end - current_begin + 1)
            current_begin = l
        current_end = max(current_end, r)

    inter_cost += 2 * (current_end - current_begin + 1)

    return inter_cost + n + 1


def bin_search(lo, hi):
    if lo + 1 >= hi:
        return lo

    mid = (lo + hi) // 2

    if cost(mid) <= t:
        lo = mid
    else:
        hi = mid

    return bin_search(lo, hi)


result = bin_search(0, m + 1)

print(result)
