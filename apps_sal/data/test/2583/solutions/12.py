import math
t = int(input())
for _ in range(t):
    n = int(input())
    cnt2 = 0
    while n % 2 == 0:
        n //= 2
        cnt2 += 1
    if n == 1 and cnt2 != 1:
        print('FastestFinger')
    elif n == 1:
        print('Ashishgup')
    elif cnt2 == 1:
        isNPrime = True
        rangeLoop = int(math.sqrt(n)) + 1
        for i in range(3, rangeLoop, 2):
            if n % i == 0:
                isNPrime = False
                break
        if isNPrime:
            print('FastestFinger')
        else:
            print('Ashishgup')
    else:
        print('Ashishgup')
