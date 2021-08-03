n = int(input())
i = 1
b = 0
while i < n:
    b = b + i * (n - i)
    i = i + 1
else:
    print(b + n)
