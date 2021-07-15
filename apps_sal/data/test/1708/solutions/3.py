import sys
n, m = map(int, input().split())
dishes = list(map(int, input().split()))
costs = list(map(int, input().split()))
cheaper = [i for i, v in sorted(enumerate(costs), key=lambda x: (x[1], x[0]), reverse=True)]

ans = []
append = ans.append

for t, d in (map(int, l.split()) for l in sys.stdin):
    t -= 1
    count = min(d, dishes[t])
    price = costs[t] * count
    dishes[t] -= count
    d -= count
    while d and cheaper:
        t = cheaper[-1]
        count = min(d, dishes[t])
        dishes[t] -= count
        if not dishes[t]:
            cheaper.pop()
        price += costs[t] * count
        d -= count

    append(0 if d else price)

print(*ans, sep="\n")
