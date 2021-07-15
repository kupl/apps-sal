from sys import stdin
from sys import stdout
from math import ceil
from math import sqrt
n = int(stdin.readline().strip())
def maxPower(num, div):
    power = 0
    while num%div == 0 and n > 1:
        num = num/div
        power += 1
    return power
primes = [2]
ans = 0
def isPrime(n):
    for i in range(2,ceil(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
if n%2 == 0:
    if n == 2:
        ans = 1
    else:
        ans = 2
else:
    isprime = isPrime(n)
    if isprime:
        ans = 1
    else:
        if isPrime(n-2):
            ans = 2
        else:
            ans = 3
stdout.write(str(ans))

