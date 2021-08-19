import math

# input
n, a, b = map(int, input().split())

# variables
x = 6 * n - 1

# main
if a * b > 6 * n:
    print(a * b)
    print(str(a) + ' ' + str(b))
    quit()

while True:
    x += 1
    for i in range(min(a, b), math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            if i >= a and x / i >= b:
                print(x)
                print(str(i) + ' ' + str(x // i))
                quit()
            if i >= b and x / i >= a:
                print(x)
                print(str(x // i) + ' ' + str(i))
                quit()
