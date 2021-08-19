a = int(input())
i = 1
amount = a
while amount > i * ((10**i) - (10**(i - 1))):
    amount = amount - i * ((10**i) - (10**(i - 1)))
    i = i + 1
x = amount // i
y = amount % i
# print(amount)
# print(i)
# print(x)
# print(y)
if y == 0:
    if i == 1:
        print(x % 10)
    else:
        print((10**(i - 1) + x - 1) % 10)
else:
    if i == 1:
        print(x % 10)
    else:
        print(((10**(i - 1) + x) // (10**(i - y))) % 10)
