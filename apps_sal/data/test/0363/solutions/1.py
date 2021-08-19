n = int(input())
v = 0
i = 1
while n >= 10 ** i:
    if i == 1:
        v += 9
    else:
        v += (10 ** i - 10 ** (i - 1)) * i
    i += 1
x = n - 10 ** (i - 1) + 1
v += i * x
print(v)
