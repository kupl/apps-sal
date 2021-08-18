n = int(input())
array = sorted(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if array[i] < array[j] and array[j] < array[k] and array[i] + array[j] > array[k]:
                count += 1

print(count)
