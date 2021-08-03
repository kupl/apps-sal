import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())

    TWO = 0
    THREE = 0

    while n % 2 == 0:
        TWO += 1
        n //= 2

    while n % 3 == 0:
        THREE += 1
        n //= 3

    if n != 1:
        print(-1)
    else:
        if TWO > THREE:
            print(-1)
        else:
            print(THREE - TWO + THREE)
