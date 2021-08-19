import random
import time
import copy
import io
import sys
n = int(input())
a = list(map(int, input().split()))
sum = 1
for a_ in a:
    if sum != -1:
        sum *= a_
    if sum != 0 and sum > pow(10, 18):
        sum = -1
    if a_ == 0:
        sum = 0
        break
print(sum)
