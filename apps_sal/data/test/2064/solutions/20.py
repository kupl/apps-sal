n = 0
one = 0
seven = 0
i = 0
j = 0

n = int(input())
if n % 2 == 0:
    for i in range(1, n // 2 + 1):
        print('1', end="")
else:
    print('7', end="")
    n = n - 3
    while n > 1:
        print('1', end="")
        n = n - 2
