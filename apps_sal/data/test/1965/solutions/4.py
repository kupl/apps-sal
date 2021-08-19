import math
t = int(input())
while t > 0:
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if all((val == x for val in a)):
        print('0')
    elif any((val == x for val in a)):
        print('1')
    elif sum((x - val for val in a)) == 0:
        print('1')
    else:
        print('2')
    t -= 1
