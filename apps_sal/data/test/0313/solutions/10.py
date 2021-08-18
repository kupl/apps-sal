n = int(input())
array = list(map(int, input().split()))
count = sum(array)
for i in range(1, n - 1):
    if array[i] == 0 and array[i - 1] == 1 and array[i + 1] == 1:
        count += 1
print(count)
