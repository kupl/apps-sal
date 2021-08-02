N = int(input())
A = list(map(int, input().split()))

min_cost = 10 ** 9 + 7
for i in range(-100, 101):
    cost = 0
    for j in range(N):
        cost += (A[j] - i) ** 2
    min_cost = min(cost, min_cost)

print(min_cost)
