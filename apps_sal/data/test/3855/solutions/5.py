n = int(input())
p = 1
x = 0
while n > 0:
    x += 1
    n -= p
    p <<= 1

print(x)
