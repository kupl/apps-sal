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
    # brr = [list(map(int,input().split())) for i in range(rows)]              # 2D array row-wise input
    n = int(input())
    # n, x = list(map(int, input().split()))
    brr = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    if(brr == sorted(brr)):
        print('Yes')
    else:
        ans = solve(arr)


'''
rows, cols = (5, 5)
arr = [[0]*cols for j in range(rows)]                                         # 2D array initialization
b=input().split()                                                             # list created by spliting about spaces
brr = [[int(b[cols*i+j]) for j in range(cols)] for i in range(rows)]          # 2D array Linear Input
rows,cols=len(brr),len(brr[0])                                                # no of rows/cols for 2D array
arr.sort(key = lambda x : x[1])                                               # sort list of tuples by 2nd element, Default priority - 1st Element then 2nd Element
s=set()                                                                       # empty set
a=maxsize                                                                     # initializing infinity
b=-maxsize                                                                    # initializing -infinity
mapped=list(map(function,input))                                              # to apply function to list element-wise
try:                                                                          # Error handling
    #code 1
except:                                                                       # ex. to stop at EOF
    #code 2 , if error occurs
'''
