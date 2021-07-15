x = int(input())

arr = [0 for i in range(x + 1)]

for i in range(2, x+1):
    if(arr[i] == 0):
        for j in range(i + i, x + 1, i):
            arr[j] = i
    arr[i] = i - arr[i] + 1;

result = x
for i in range(arr[x], x + 1):
    result = min(result, arr[i])

print(result)

