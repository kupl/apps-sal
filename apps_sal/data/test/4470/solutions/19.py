"""
NTC here
"""
from sys import setcheckinterval, stdin
setcheckinterval(1000)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


for _ in range(iin()):
    n = iin()
    ans = 0
    while n != 1:
        ans += 1
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n = 2 * (n // 3)
        elif n % 5 == 0:
            n = 4 * (n // 5)
        else:
            print(-1)
            break
    else:
        print(ans)
