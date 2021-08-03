import fractions
import math
n = int(input())
#a,b=map(int,input().split(' '))
#n=list(map(int,input().split(' ')))
t = list(map(int, input().split(' ')))
a = set(t)
print(n + 1 - len(a))
