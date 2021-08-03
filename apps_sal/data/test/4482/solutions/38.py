n = int(input())
a = list(map(int, input().split()))

result = 10**9
for num in range(-100, 101):
    cost = 0
    for i in range(n):
        cost += (a[i] - num) ** 2
    result = min(result, cost)
print(result)
