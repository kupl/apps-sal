import sys
import math

n = int(input())

a = [int(input()) for i in range(5)]

print((math.ceil(n/min(a))+4))

