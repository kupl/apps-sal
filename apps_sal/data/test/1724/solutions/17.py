'''input
2
3 8
10
'''
from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict
from bisect import bisect_left

# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
barr = list(stdin.readline().strip())
prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]
mx = 0
temp = 0
for i in range(n - 1, -1, -1):
    if barr[i] == '1':
        if i >= 1:
            mx = max(mx, temp + prefix[i - 1])
        temp += arr[i]
    # print(temp, mx)
mx = max(mx, temp)
print(mx)
