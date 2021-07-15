import sys
x = int(input())

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if (x == 2):
    print(1)
    return

if (x == 4 or x == 6):
    print(2)
    return

if (x % 2 == 0):
    print(2)	
    return

else:
    if (is_prime(x)):
        print(1)
        return
    else:
        if (is_prime(x -2)):
            print(2)
            return
        else:
            print(3)
            return

