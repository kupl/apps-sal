(n, k) = list(map(int, input().split()))
sum = 0
arr = list(map(int, input().split()))
for i in range(0, n):
    sum = sum + arr[i] // 10
    temp = arr[i] // 10
    arr[i] = temp * 10 + 10 - arr[i]
arr.sort()
for i in range(0, n):
    if k >= arr[i]:
        k = k - arr[i]
        sum = sum + 1
    else:
        break
sum = sum + k // 10
if sum > 10 * n:
    sum = 10 * n
print(sum)
