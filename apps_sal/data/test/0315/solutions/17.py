n, k = list(map(int, input().split()))

a = list(map(int, input().split()))

result = 0

for i in range(1, n):
    if a[i] + a[i-1] < k:
        result += k - a[i] - a[i-1]
        a[i] = (k - a[i-1])
print(result)
print(" ".join(map(str, a)))

