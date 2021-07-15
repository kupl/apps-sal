from sys import stdin as cin,stdout as cout
from math import factorial as f
from itertools import combinations as comb
n,d = list(map(int,(cin.readline().split())))
a = list(map(int,(cin.readline().split())))
s = sum(a)
r = d-s-(n-1)*10
if r <0:
    print(-1)
else:
    print(int((d-s)/5))



