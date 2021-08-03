'''input
2
3 6
'''
from sys import stdin, setrecursionlimit
from bisect import bisect_right
import math
setrecursionlimit(15000)


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
for i in range(n):
    arr[i] = abs(arr[i])
arr.sort()
count = 0
for i in range(n):
    index = bisect_right(arr, arr[i] * 2)
    count += index - i - 1
print(count)
