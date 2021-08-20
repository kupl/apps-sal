(n, m, k) = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] += a[i - 1]
for i in range(1, m + 1):
    b[i] += b[i - 1]
(ans, j) = (0, m)
for i in range(n + 1):
    if a[i] > k:
        break
    while a[i] + b[j] > k:
        j -= 1
    if i + j > ans:
        ans = i + j
print(ans)
