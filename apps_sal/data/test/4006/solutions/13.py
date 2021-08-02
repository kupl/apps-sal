n = int(input())
t = 0
while n > 9:
    n += 1
    while n % 10 == 0:
        n //= 10
    t += 1
print(t + 9)
