
tt = int(input())

for loop in range(tt):

    n = int(input())

    x = 2
    while x ** 2 <= n:
        if n % x == 0:
            break
        x += 1
    else:
        print(1, n - 1)
        continue

    print(n // x, n - n // x)
