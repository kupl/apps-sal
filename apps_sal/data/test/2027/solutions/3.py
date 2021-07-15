n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    print(arr[i] + arr[i + 1], end = ' ')
print(arr[i + 1])
