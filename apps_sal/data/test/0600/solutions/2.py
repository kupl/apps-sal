a = int(input())
b = int(input())
middle = (a + b) // 2
d1 = abs(a - middle)
d2 = abs(b - middle)
print(d1 * (d1 + 1) // 2 + d2 * (d2 + 1) // 2)
