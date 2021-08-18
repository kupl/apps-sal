import heapq
arr = input()
N, K = [int(x) for x in arr.split(' ')]

arr = input()
arr = [int(x) for x in arr.split(' ')]

arr.sort()
data = [[0] * N for _ in range(K)]

left = 0
right = 0

res = 0
while left < N and right < N:
    if arr[right] > arr[left] + 5:
        left += 1
    else:
        data[0][right] = max(data[0][right - 1], right - left + 1)
        right += 1

for i in range(K):
    data[i][0] = 1


for j in range(1, K):
    left = 0
    right = 0

    res = 0
    while left < N and right < N:
        if arr[right] > arr[left] + 5:
            left += 1
        else:
            if left >= 1 and right >= 1:
                data[j][right] = max(data[j][right - 1], data[j][right], data[j - 1][left - 1] + right - left + 1)
            elif left == 0 and right >= 1:
                data[j][right] = max(data[j][right - 1], data[j][right], right - left + 1)
            right += 1


print(data[K - 1][N - 1])
