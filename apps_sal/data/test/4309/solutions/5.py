n = int(input())

h = n // 100
x = h * 100 + h * 10 + h
print(x) if n <= x else print(x + 111)
