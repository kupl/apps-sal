n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
arr.sort()
minD = 3 * 10 ** 9
for i in range(1, n):
    minD = min(minD, arr[i] - arr[i - 1])
count = 0
for i in range(1, n):
    if arr[i] - arr[i - 1] == minD:
        count += 1
print(minD, count)
