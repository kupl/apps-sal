(n, m) = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = sorted(list(map(int, input().split())))
best = float('inf')
for item in arr2:
    diff = item - arr1[0] if item >= arr1[0] else m - arr1[0] + item
    new = [(arr1[i] + diff) % m for i in range(n)]
    if sorted(new) == arr2:
        best = min(best, diff)
print(best)
