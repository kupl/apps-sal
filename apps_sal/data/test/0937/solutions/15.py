(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
num1 = 0
for i in range(n):
    if b[i] == 0:
        c[i] = a[i]
    else:
        num1 += a[i]
num2 = 0
s = sum(c[:k])
for i in range(n - k + 1):
    num2 = max(num2, num1 + s)
    if i != n - k:
        s = s - c[i] + c[i + k]
print(num2)
