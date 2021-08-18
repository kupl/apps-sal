from collections import defaultdict


def possible(days):
    nonlocal events, k

    latest_ev = defaultdict(int)
    for d, t in events:
        if d <= days:
            latest_ev[t] = max(latest_ev[t], d)

    earned = days
    offers_needed = 2 * sum(k) - earned

    offers = 0
    cur_day = 0
    cur_val = 0
    for t, d in sorted(list(latest_ev.items()), key=lambda x: x[1]):
        cur_val += d - cur_day
        cur_day = d
        offers_to_take = min(k[t], cur_val)
        offers += offers_to_take
        cur_val -= offers_to_take
    return offers >= offers_needed


n, m = list(map(int, input().split()))

k = list(map(int, input().split()))

events = []
for _ in range(m):
    d, t = list(map(int, input().split()))
    t -= 1
    events.append((d, t))

lo = 0
hi = 4 * 10**5

while lo + 1 < hi:
    mid = (lo + hi) // 2

    if possible(mid):
        hi = mid
    else:
        lo = mid

print(hi)
