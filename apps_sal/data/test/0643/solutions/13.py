import math
import sys
t = int(input())
for j in range(1, (t + 1)):
    x, y, p, q = (list(map(int, input().split())))
    f1 = 0
    if(p != q and p != 0):
        tmp = max(((y - x) + (q - p) - 1) // (q - p), (x + p - 1) // p)
        # print(tmp)
        # include<FU*k> test case
        print((q * tmp) - y)
        f1 = 1

    if(p == 0 and x == 0):
        print(0)
    elif(p == q and x == y):
        print(0)
    elif (not f1):
        print(-1)
