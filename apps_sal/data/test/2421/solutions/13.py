n = int(input())
for _ in range(n):
    (y, x) = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    for i in range(36):
        costs[i % 6] = min(costs[i % 6], costs[(i + 5) % 6] + costs[(i + 1) % 6])
    ans = 0
    if x >= 0:
        if y >= 0:
            if x >= y:
                ans = (x - y) * costs[1] + y * costs[0]
            else:
                ans = x * costs[0] + (y - x) * costs[5]
        else:
            ans = x * costs[1] - y * costs[2]
    elif y >= 0:
        ans = -x * costs[4] + y * costs[5]
    elif x <= y:
        ans = (y - x) * costs[4] - y * costs[3]
    else:
        ans = -x * costs[3] + (x - y) * costs[2]
    print(ans)
