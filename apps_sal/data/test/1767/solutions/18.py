n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(1, n):
    a[i] = a[i] | a[i - 1]
    b[i] = b[i] | b[i - 1]
print(a[n - 1] + b[n - 1])
