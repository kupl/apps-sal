zc = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]

n = int(input())

if (n == 0):
    print(1)
else:
    sum = 0
    while (n):
        sum += zc[n % 16]
        n //= 16
    print(sum)
