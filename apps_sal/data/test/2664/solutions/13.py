import sys
import random
n = random.randint(1, 5)
d = dict()
d = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
d[n] = 2
print(1)
sys.stdout.flush()
print('5 1 1 2 2 3')
sys.stdout.flush()
print('5 3 4 4 5 5')
sum1 = 2 * (d[1] + d[2]) + d[3]
sum2 = 2 * (d[4] + d[5]) + d[3]
sys.stdout.flush()
if sum1 == sum2:
    print(2)
    sys.stdout.flush()
    print(3)
    sys.exit()
elif sum1 < sum2:
    print(1)
    sys.stdout.flush()
    print('1 4')
    sys.stdout.flush()
    print('1 5')
    sys.stdout.flush()
    if d[4] < d[5]:
        print(2)
        sys.stdout.flush()
        print(5)
        sys.exit()
    else:
        print(2)
        sys.stdout.flush()
        print(4)
        sys.exit()
else:
    print(1)
    sys.stdout.flush()
    print('1 1')
    sys.stdout.flush()
    print('1 2')
    sys.stdout.flush()
    if d[1] < d[2]:
        print(2)
        sys.stdout.flush()
        print(2)
        sys.exit()
    else:
        print(2)
        sys.stdout.flush()
        print(1)
        sys.exit()
