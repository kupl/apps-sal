__author__ = '$'
import sys


def GCD(x, y):
    return x if y == 0 else GCD(y, x % y)


try:
    while True:
        n = int(input())
        val = list(map(int, input().split(' ')))
        res = val[0]
        for i in range(n - 1):
            res = GCD(res, val[i + 1])
        ans = True
        for i in range(n):
            tmp = val[i] // res
            while tmp != 1:
                if tmp % 2 == 0:
                    tmp //= 2
                elif tmp % 3 == 0:
                    tmp //= 3
                else:
                    ans = False
                    break
            if not ans:
                break
        print('Yes' if ans else 'No')
except EOFError:
    pass
