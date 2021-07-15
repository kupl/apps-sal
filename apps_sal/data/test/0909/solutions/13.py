a = int(input())
b = int(input())
c = int(input())
res =max(a + b + c, a + b * c, (a + b) * c, a * b + c, a * (b + c), a * b * c)

print(res)

