N = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))
ans = 0
for i in range(N):
    if values[i] - costs[i] > 0:
        ans += values[i] - costs[i]
print(ans)
