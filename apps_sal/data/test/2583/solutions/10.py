import sys
from collections import deque


def pprint(s): return print(' '.join(map(str, s)))
def input(): return sys.stdin.readline().strip()


ipnut = input


def is_prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(int(input())):
    n = int(input())
    if n == 1:
        print('FastestFinger')
    elif n % 2 == 0:
        k = 0
        while n % 2 == 0:
            n //= 2
            k += 1
        if n == 1:
            if k == 1:
                print('Ashishgup')
            else:
                print('FastestFinger')
        else:
            if k == 1:
                if is_prime(n):
                    print('FastestFinger')
                else:
                    print('Ashishgup')
            else:
                print('Ashishgup')
    else:
        print('Ashishgup')
