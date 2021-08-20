n = int(input())
arr = list(map(int, input().split()))
res = [0] * n
arr.sort()
for i in range(n):
    if i < n // 2:
        res[i * 2 + 1] = arr[i]
    else:
        res[(i - n // 2) * 2] = arr[i]
x = 0
for i in range(1, n - 1):
    if res[i - 1] > res[i] < res[i + 1]:
        x += 1
print(x)
print(*res)
