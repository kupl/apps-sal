n = int(input())
arr = list(map(int, input().strip().split(' ')))
a = [0 for i in range(200001)]
b = [0 for i in range(200001)]
for i in arr:
    a[i] += 1
j = 1
t = 0
for i in range(1, n + 1):
    if(a[i] > 0):
        t += 1
for i in range(n):
    if(a[arr[i]] > 1):
        while(a[j] != 0):
            j += 1
        if(arr[i] > j or b[arr[i]] == 1):
            a[arr[i]] -= 1
            arr[i] = j
            a[j] = 1
        else:
            b[arr[i]] = 1
print(n - t)
for i in arr:
    print(i, end=' ')
print()
