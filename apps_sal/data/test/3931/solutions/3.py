n, a, b, k, f = [int(i) for i in input().split()]
stops = dict()
prev = ""
ans = 0
for i in range(n):
    x, y = [i for i in input().split()]
    price = a
    if x == prev:
        price = b
    prev = y
    p, q = (min(x, y), max(x, y))
    if (p, q) in stops:
        stops[(p, q)] += price
    else:
        stops[(p, q)] = price
    ans += price
edge_cost = sorted([stops[key] for key in stops], reverse=True)
for i in edge_cost:
    if k > 0 and f < i:
        ans = ans - i + f
    else:
        break
    k -= 1
print(ans)
