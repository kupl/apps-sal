n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for i in range(m):
    (a, b) = list(map(int, input().split()))
    a -= 1
    if a > 0:
        arr[a - 1] += b - 1
    if a < n - 1:
        arr[a + 1] += arr[a] - b
    arr[a] = 0
for i in range(n):
    print(arr[i])
