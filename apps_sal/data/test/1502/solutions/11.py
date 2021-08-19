n = int(input())
a = n // 8
b = n % 8 // 4
c = n % 4 // 2
d = n % 2
a = not a
b = not b if a else b
c = not c if a and b else c
d = not d if a and b and c else d
print(1 * d + 2 * c + 4 * b + 8 * a)
