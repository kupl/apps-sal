(a, b) = map(int, input().split())
str1 = str(a) * b
str2 = str(b) * a
print(min(str1, str2))
