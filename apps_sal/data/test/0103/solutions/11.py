n = int(input())
arr = [0] + [int(x) for x in input().split()] + [1001]
arr2 = []
for (a, b) in zip(arr, arr[1:]):
    arr2.append(b - a)
longest = 0
current = 0
for x in arr2:
    if x == 1:
        current += 1
    else:
        longest = max(longest, current)
        current = 0
longest = max(longest, current)
print(max(longest - 1, 0))
