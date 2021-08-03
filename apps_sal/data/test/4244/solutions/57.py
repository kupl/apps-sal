N = int(input())
X = list(map(int, input().split()))
cost = 10**18
for i in range(1, 101):
    cost_count = 0
    for j in range(N):
        cost_count += (X[j] - i)**2
    if cost > cost_count:
        cost = cost_count
    else:
        pass
print(cost)
