import sys
#sys.stdin = open("in.txt" , "r")
#sys.stdout = open("out.txt" , "w")
from math import ceil
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

m,d = list(map(int,input().split()))
days = d - 1 + days[m] 
print(ceil(days/7))

