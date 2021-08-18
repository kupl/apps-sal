from math import factorial

n = int(input())
AA = input()
AB = input()
BA = input()
BB = input()

mod = pow(10, 9) + 7

if n == 2 or n == 3:
    print(1)
    return

if AB == 'B':
    if BB == 'B':
        print(1)
    else:
        if BA == 'B':
            count = 0
            n -= 2
            m = 0
            while n >= 0:
                count += factorial(n + m) // (factorial(n) * factorial(m))
                count %= mod
                n -= 2
                m += 1
            print(count)
        else:
            print(pow(2, n - 3, mod))
else:
    if AA == 'A':
        print(1)
    else:
        if BA == 'A':
            count = 0
            n -= 2
            m = 0
            while n >= 0:
                count += factorial(n + m) // (factorial(n) * factorial(m))
                count %= mod
                n -= 2
                m += 1
            print(count)
        else:
            print(pow(2, n - 3, mod))
