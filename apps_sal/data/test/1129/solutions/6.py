'''
You are given n points on a line with their coordinates x_i. 
Find the point x so the sum of distances to the given points is minimal.
Input

The first line contains integer n (1 ≤ n ≤ 3·105) 
— the number of points on the line.

The second line contains n integers x[i] ( - 109 ≤ x[i] ≤ 109) 
— the coordinates of the given n points.

Output

Print the only integer x — the position of the optimal point on the line. 
If there are several optimal points print the position of the 
leftmost one. It is guaranteed that the answer is always the integer.
'''

import io
import sys
import time
import random


n = int(input())
x = [int(x) for x in input().split()]

x.sort()
if len(x) % 2 == 0:
    print(x[(len(x) - 1) // 2])
else:
    print(x[len(x) // 2])
