(n, b) = [int(v) for v in input().split()]
a = [int(v) for v in input().split()]
(n_odd, n_even) = (0, 0)
costs = []
for i in range(n - 1):
    if a[i] % 2 == 0:
        n_even += 1
    else:
        n_odd += 1
    if n_even == n_odd:
        costs.append(abs(a[i] - a[i + 1]))
costs.sort()
ans = 0
while ans < len(costs) and costs[ans] <= b:
    b -= costs[ans]
    ans += 1
print(ans)
