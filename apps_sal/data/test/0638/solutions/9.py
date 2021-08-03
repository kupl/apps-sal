'''input
5 100
80 40 40 40 60
'''
# problem solving is essentially pattern recognition
from sys import stdin, stdout
import math
import collections

# main starts
n, m = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
aux = []
for i in range(len(arr)):
    aux.sort()
    count = 0
    j = len(aux)
    while sum(aux[: j]) + arr[i] > m:
        j -= 1
        count += 1
    print(count, end=' ')
    aux.append(arr[i])
