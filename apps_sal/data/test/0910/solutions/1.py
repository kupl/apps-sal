import sys
(n, a, b) = [int(x) for x in input().strip().split(' ')]
if n > a * b:
    print(-1)
else:
    for i in range(a):
        if b % 2 == 0 and i % 2 == 0:
            for j in reversed(range(b)):
                number = i * b + j + 1
                if number > n:
                    print(0, ' ', end='')
                else:
                    print(number, ' ', end='')
        else:
            for j in range(b):
                number = i * b + j + 1
                if number > n:
                    print(0, ' ', end='')
                else:
                    print(number, ' ', end='')
        print()
