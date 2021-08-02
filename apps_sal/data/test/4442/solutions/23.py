a, b = input().split()
str = ''
if int(a) <= int(b):
    for _ in range(int(b)):
        str += a
else:
    for _ in range(int(a)):
        str += b

print(str)
