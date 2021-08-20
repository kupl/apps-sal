n = int(input())
while n ** 0.5 % 1 != 0:
    n -= 1
print(n)
