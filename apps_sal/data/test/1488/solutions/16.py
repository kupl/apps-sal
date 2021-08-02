'''input
4
1 5 77 2
'''
from sys import stdin
import collections
import math


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr.sort()

numerator = sum(arr)
temp = 0
for i in range(n):
    temp += i * arr[i]
for i in range(n - 1, -1, -1):
    temp -= arr[n - 1 - i] * i

numerator += 2 * temp
g = math.gcd(numerator, n)
print(numerator // g, n // g)
