def mi():
    return list(map(int, input().split()))


'''

'''


def isPrime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


for _ in range(int(input())):
    n = int(input())
    nc = n
    if n % 2 and n > 1:
        winner = 1
    elif n == 1:
        winner = 2
    elif n == 2:
        winner = 1
    else:
        while n % 2 == 0:
            n //= 2

        if n % 2 and n > 1:
            if nc // n > 2:
                winner = 1
            elif isPrime(n):
                winner = 2
            else:
                winner = 1
        else:
            winner = 2

    if winner == 1:
        print('Ashishgup')
    else:
        print('FastestFinger')
