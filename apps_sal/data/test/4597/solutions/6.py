n = int(input())
pow = 1
for i in range(n):
    pow *= i + 1
    pow = pow % (10 ** 9 + 7)
print(pow)
