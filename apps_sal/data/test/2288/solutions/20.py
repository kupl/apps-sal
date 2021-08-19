from sys import *


def solve(b):
    (c1, c2) = (0, 0)
    for el in b:
        if el == 1:
            c1 += 1
        else:
            c2 += 1
    if c1 == 0 or c2 == 0:
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
    if brr == sorted(brr):
        print('Yes')
    else:
        ans = solve(arr)
'\nrows, cols = (5, 5)\narr = [[0]*cols for j in range(rows)]                                         # 2D array initialization\nb=input().split()                                                             # list created by spliting about spaces\nbrr = [[int(b[cols*i+j]) for j in range(cols)] for i in range(rows)]          # 2D array Linear Input\nrows,cols=len(brr),len(brr[0])                                                # no of rows/cols for 2D array\narr.sort(key = lambda x : x[1])                                               # sort list of tuples by 2nd element, Default priority - 1st Element then 2nd Element\ns=set()                                                                       # empty set\na=maxsize                                                                     # initializing infinity\nb=-maxsize                                                                    # initializing -infinity\nmapped=list(map(function,input))                                              # to apply function to list element-wise\ntry:                                                                          # Error handling\n    #code 1\nexcept:                                                                       # ex. to stop at EOF\n    #code 2 , if error occurs\n'
