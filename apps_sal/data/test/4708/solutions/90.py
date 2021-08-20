n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n > k:
    total = k * x + (n - k) * y
    print(total)
else:
    total = n * x
    print(total)
