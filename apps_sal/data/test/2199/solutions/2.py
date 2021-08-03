import sys
import math
from collections import defaultdict
# n=int(sys.stdin.readline().split())
arr = []
q = int(sys.stdin.readline())
a, b = list(map(int, sys.stdin.readline().split()))
l, r = 0, 0
mean = b
num = 1
arr.append(b)
for _ in range(1, q):
    lis = list(map(int, sys.stdin.readline().split()))
    if lis[0] == 1:
        b = lis[1]
        arr.append(b)
        if len(arr) == 2:
            newmean = (arr[0] + arr[1]) / 2
            r += 1
            mean = newmean
            num = 2
            continue
        newmean = (mean * num - arr[r] + arr[r + 1]) / num
        r += 1
        mean = newmean
        while l + 1 < r and (mean * num + arr[l + 1]) / (num + 1) <= mean:
            mean = (mean * num + arr[l + 1]) / (num + 1)
            l += 1
            num += 1
    else:
        # print(arr,'arr',mean,'mean')
        print(arr[r] - mean)
