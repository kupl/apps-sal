(n, k1, k2) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(abs(a[i] - b[i]))
arr = sorted(arr, reverse=True)
for i in range(k1 + k2):
    arr[0] = abs(arr[0] - 1)
    j = 0
    while j < n - 1 and arr[j] < arr[j + 1]:
        (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
        j += 1
ans = 0
for i in range(n):
    ans = ans + arr[i] * arr[i]
print(ans)
