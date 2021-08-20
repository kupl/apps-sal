import math
import time
(a, b) = [int(i) for i in input().split()]
if a < b:
    print(0)
elif a == b:
    print('infinity')
else:

    def FindRequiredDivisors(x, b):
        y = 1
        ans = 0
        while y <= int(math.sqrt(x)):
            if x % y == 0:
                if y != int(x / y):
                    if y > b:
                        ans += 1
                    if int(x / y) > b:
                        ans += 1
                elif y == int(x / y) and y > b:
                    ans += 1
            y += 1
        return ans
    print(FindRequiredDivisors(a - b, b))
