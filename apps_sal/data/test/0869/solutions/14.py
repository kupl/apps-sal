a, b = list(map(int, str.split(input())))
print(min(a, b), abs(a - b) // 2)
