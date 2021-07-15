n = int(input())
s = input()
b = s.split()
for i in range(0, n):
    b[i] = int(b[i])
a = [0] * n
for i in range(0, n - 1):
    a[i] = str(b[i] + b[i + 1])
a[n - 1] = str(b[n - 1])
print(" ".join(a))

