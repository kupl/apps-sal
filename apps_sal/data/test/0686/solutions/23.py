from sys import *
from heapq import *



for q in range(int(input())):
    x, y = map(int, input().split())
    if x > y + 1:
        print("YES")
    else:
        print("NO")
    
'''
1
8
100 200 100 200 100 200 100 100
10 2
15 3
107
3
''' 
