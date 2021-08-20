(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = 0
b = a[0]
for i in range(1, n):
    if b + a[i] < k:
        s += k - b - a[i]
        a[i] = k - b
    b = a[i]
print(s)
print(*a)
