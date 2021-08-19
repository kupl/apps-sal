(a, b) = input().split()
str_a = a * int(b)
str_b = b * int(a)
print(str_a if str_a < str_b else str_b)
