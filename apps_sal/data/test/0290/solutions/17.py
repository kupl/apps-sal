n = int(input())
j = int(n ** 0.5)
if n == j ** 2:
    print(2 * j)
elif n <= j * (j + 1):
    print(2 * j + 1)
else:
    print(2 * j + 2)
