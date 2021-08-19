n = int(eval(input()))
a = 3
while n % a == 0:
    a *= 3
print(n // a + 1)
