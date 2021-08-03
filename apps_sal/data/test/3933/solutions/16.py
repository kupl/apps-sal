n = int(input())
arr = list(map(int, input().split()))

m = arr[0] - arr[1]
x = True
for i in range(1, n):
    if (arr[i - 1] - arr[i] == m):
        continue
    else:
        x = False
if x == True:
    print(arr[n - 1] - m)
else:
    print(arr[n - 1])
