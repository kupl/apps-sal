n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n <= k:
    print(n * x)
else:
    tmp = (n - k) * y + k * x
    print(tmp)
