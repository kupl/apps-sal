__author__ = 'User'
n = int(input())
arr = list(map(int, input().split()))
mx = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    #print(arr[i], mx[i + 1])
    mx[i] = max(mx[i + 1], arr[i])
for j in range(n):
    if mx[j + 1] >= arr[j]:
        print(mx[j] - arr[j] + 1, end = " ")
    else:
        print(0, end = " ")
