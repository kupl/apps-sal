(n, k) = map(int, input().split())
cost = [0] + list(map(int, input().split()))
capitals = set(map(int, input().split()))
town_sum = [0] * (n + 1)
no_cap_sum = [0] * (n + 2)
for i in range(1, n + 1):
    town_sum[i] = town_sum[i - 1] + cost[i]
    if i in capitals:
        no_cap_sum[i] = no_cap_sum[i - 1]
    else:
        no_cap_sum[i] = no_cap_sum[i - 1] + cost[i]
ans = 0
for i in range(1, n + 1):
    if i in capitals:
        ans += (town_sum[n] - town_sum[i]) * cost[i]
        ans += no_cap_sum[i - 2] * cost[i]
    elif i < n:
        ans += cost[i] * cost[i + 1]
    elif i == n and 1 not in capitals:
        ans += cost[1] * cost[i]
print(ans)
