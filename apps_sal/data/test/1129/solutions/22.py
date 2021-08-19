n = int(input())
array = list(map(int, input().split()))
array.sort()
summ = sum(array)
summ2 = 0
differences = [0] * n
for i in range(n):
    differences[i] = summ - (summ2 + array[i]) - summ2
    summ2 += array[i]
dist = [0] * n
for i in range(n):
    dist[i] = array[i] * i + differences[i] - array[i] * (n - i - 1)
minId = 0
for i in range(n):
    if dist[i] < dist[minId]:
        minId = i
print(array[minId])
