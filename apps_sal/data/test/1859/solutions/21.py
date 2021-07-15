import sys
from math import ceil, sqrt

input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print(int(n/2))
else:
    prime = n
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            prime = i
            break
    print(1 + int((n - prime)/2))
