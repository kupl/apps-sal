n = int(input())
a = list(map(int, input().split()))
k = min(a[0], a[-1]) // (n - 1)
for i in range(1, n - 1):
    k = min(k, min(a[0], a[i]) // i, min(a[i], a[-1]) // (n - 1 - i))
print(k)
