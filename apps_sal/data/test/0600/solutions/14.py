
a = int(input())
b = int(input())

n = abs(b - a)

t = n // 2
if n % 2:
    print((2 * t * (t + 1) // 2) + (t + 1))
else:
    print(2 * t * (t + 1) // 2)
