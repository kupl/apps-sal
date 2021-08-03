__author__ = 'user'
n = int(input())
arr = [int(x) for x in input().split()]
i = 0
a = abs(arr[i] - arr[i + 1])
b = abs(arr[i] - arr[n - 1])
print(a, b)
for i in range(1, n - 1):
    a = min(abs(arr[i] - arr[i - 1]), abs(arr[i] - arr[i + 1]))
    b = max(abs(arr[i] - arr[0]), abs(arr[i] - arr[n - 1]))
    print(a, b)
i = n - 1
a = abs(arr[i] - arr[i - 1])
b = abs(arr[i] - arr[0])
print(a, b)
