arr = list(map(int, input().split()))
n = arr[0]
k = arr[1]
for i in range(k):
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1
print(n)
