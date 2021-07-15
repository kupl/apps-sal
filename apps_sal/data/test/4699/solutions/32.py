n, k = map(int, input().split())
arr = list(map(int, input().split()))

inf = float('inf')
min_cost = inf
for amount in range(n, 100000):
    for i, e in enumerate(arr):
        if str(e) in str(amount):
            break
        if i == len(arr)-1:
            min_cost = min(min_cost, amount)

print(min_cost)
