import sys
import math
import random

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
suma = 0
sumb = 0
for elem in a:
    suma += elem
for elem in b:
    sumb += elem

if sumb <= suma:
    print('Yes')
else:
    print('No')
