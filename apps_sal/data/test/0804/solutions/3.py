from sys import stdin, stdout
import random


s = list(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())
sLen = len(s)
sSet = set(s)
diffLet = len(sSet)

if k > 26 or k > sLen:
    print('impossible')
elif k <= diffLet:
    print(0)
else:
    print(k - diffLet)
