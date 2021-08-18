a = int(input())
b = int(input())
mid = (a + b) // 2

a = abs(mid - a)
b = abs(mid - b)
print((a * (a + 1)) // 2 + (b * (b + 1)) // 2)
