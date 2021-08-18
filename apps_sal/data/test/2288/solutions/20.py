from sys import *


def solve(b):
    c1, c2 = 0, 0
    for el in b:
        if(el == 1):
            c1 += 1
        else:
            c2 += 1
    if(c1 == 0 or c2 == 0):
        print('No')
    else:
        print('Yes')
    pass


test = 1
test = int(input())
for t in range(0, test):
    n = int(input())
    brr = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    if(brr == sorted(brr)):
        print('Yes')
    else:
        ans = solve(arr)


'''
rows, cols = (5, 5)
arr = [[0]*cols for j in range(rows)]                                         
b=input().split()                                                             
brr = [[int(b[cols*i+j]) for j in range(cols)] for i in range(rows)]          
rows,cols=len(brr),len(brr[0])                                                
arr.sort(key = lambda x : x[1])                                               
s=set()                                                                       
a=maxsize                                                                     
b=-maxsize                                                                    
mapped=list(map(function,input))                                              
try:                                                                          
except:                                                                       
'''
