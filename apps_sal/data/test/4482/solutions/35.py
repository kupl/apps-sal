N = int(input())
A = list(map(int, input().split()))
costs = []
for i in range(101):
    cost = 0
    for j in range(N):
        cost += (A[j] - i) ** 2
    costs.append(cost)
    cost = 0
    for j in range(N):
        cost += (A[j] + i) ** 2
    costs.append(cost)
print(min(costs))
