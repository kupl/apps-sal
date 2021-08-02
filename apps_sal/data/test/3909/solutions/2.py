n = int(input())
t = 1
while n % t == 0:
    t *= 3
print(n // t + 1)
