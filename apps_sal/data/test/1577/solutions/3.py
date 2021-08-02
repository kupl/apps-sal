import sys
import math
n = int(input())
s = input()
a = s.count('A')
b = n - a
if a == b:
    print('Friendship')
elif b > a:
    print('Danik')
else:
    print('Anton')
