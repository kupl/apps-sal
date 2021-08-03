n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n > k:
    print(x * k + y * (n - k))
else:
    print(x * n)
