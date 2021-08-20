n = int(input())
l = 0
k = 0
arr = list(map(int, input().split()))
for i in range(0, n):
    if arr[i] % 2 == 0:
        l = l + 1
    if arr[i] % 2 == 1:
        k = k + 1
if l > k:
    print(k)
else:
    print(l + (k - l) // 3)
