import math


def IsPrime(x):
    if x <= 2:
        return x == 2
    top = int(math.sqrt(x)) + 1
    for i in range(2, top):
        if x % i == 0:
            return False
    return True


val = int(input())
if val == 1:
    print('1')
elif IsPrime(val):
    print(val)
else:
    cnt = 0
    top = int(math.sqrt(val)) + 1
    for i in range(2, top):
        if val % i == 0:
            cnt += 1
            while val % i == 0:
                val /= i
            if val == 1:
                print(i)
            else:
                print('1')
            return
