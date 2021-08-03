n, m = list(map(int, input().split()))
keys = []

for _ in range(m):
    cost, types = list(map(int, input().split()))
    to_open = list(map(int, input().split()))
    keys.append([cost, to_open])

DP = [10**9] * (2**n)
DP[0] = 0

for cost, (to_open) in keys:
    openable = 0
    for open in to_open:
        openable |= 1 << (open - 1)

    for opened in range(2 ** n):
        pattern = opened | openable
        DP[pattern] = min(DP[pattern], DP[opened] + cost)

full_open = 2**n - 1
ans = DP[full_open]

if ans == 10 ** 9:
    ans = -1

print(ans)
