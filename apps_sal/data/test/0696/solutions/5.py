from fractions import gcd
t = 0
x = int(input()) - 1
for i in range(1, x + 1):
    if gcd(x, i) == 1:
        t += 1
print(t)
