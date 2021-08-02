n = int(input())
y = 1
d = 0
while y <= n:
    y += 10**d
    if y // 10**(d + 1) == 1:
        d += 1
print(y - n)
