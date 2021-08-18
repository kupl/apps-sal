from collections import Counter, defaultdict

n, m = [int(c) for c in input().split()]
xs = [int(c) for c in input().split()]


def ring_cost(fr, to):
    return to - fr if to >= fr else (m - fr) + to


from_counter = Counter(xs[:-1])
to_counter = Counter(xs[1:])

fav = 1
cost = 0
use_fav = 0
nofav_cost = defaultdict(int)

for i in range(n - 1):
    normal_cost = ring_cost(xs[i], xs[i + 1])
    fav_cost = ring_cost(fav, xs[i + 1]) + 1
    cost += min(normal_cost, fav_cost)
    nofav_cost[xs[i + 1]] += normal_cost
    if fav_cost <= normal_cost:
        use_fav += 1

ans = cost
for fav in range(2, m + 1):
    stop_using_fav = to_counter[fav - 1]
    use_fav -= stop_using_fav
    cost += nofav_cost[fav - 1] - stop_using_fav

    cost -= use_fav

    use_fav += from_counter[fav - 1]
    ans = min(ans, cost)

print(ans)
