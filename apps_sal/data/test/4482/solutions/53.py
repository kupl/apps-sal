n = int(input())
arr = list(map(int, input().split()))

mini = min(arr)
maxi = max(arr)
cost = 10000000000

for i in range(-100, 101 + 1):
    add = 0
    for j in range(n):
        add = add + (arr[j] - i)**2
    cost = min(cost, add)
print(cost)
