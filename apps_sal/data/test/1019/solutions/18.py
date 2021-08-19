from sys import stdin, stdout
import math
n = int(stdin.readline().rstrip())
if n % 2 == 0:
    n1 = n // 2
else:
    n1 = n // 2
foundGCD = False
for i in range(n1, 1, -1):
    n2 = n - i
    if math.gcd(i, n2) == 1:
        foundGCD = True
        print(str(i) + ' ' + str(n2))
        break
if not foundGCD:
    print(str(1) + ' ' + str(n - 1))
