import sys
input = sys.stdin.readline
(sol_n, n, trap_n, t) = [int(item) for item in input().split()]
sold = [int(item) for item in input().split()]
sold.sort(reverse=True)
trap = []
for i in range(trap_n):
    (l, r, d) = [int(item) for item in input().split()]
    trap.append((d, l, r))
trap.sort()
ll = 0
rr = sol_n + 1
while rr - ll > 1:
    mid = (ll + rr) // 2
    to_save = sold[mid - 1]
    alone_walk = [0] * (n + 1)
    for (d, l, r) in trap:
        if d > to_save:
            alone_walk[l - 1] += 1
            alone_walk[r] -= 1
    total = 0
    time = 0
    for item in alone_walk:
        total += item
        if total > 0:
            time += 2
    time += n + 1
    if time <= t:
        ll = mid
    else:
        rr = mid
print(ll)
