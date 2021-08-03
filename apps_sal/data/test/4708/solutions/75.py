n = int(input())
k = int(input())
x = int(input())
y = int(input())

n1 = n - k
if n > k:
    print((k * x) + (y * n1))
else:
    print(n * x)
