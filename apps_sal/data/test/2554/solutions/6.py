import math
import sys
from itertools import permutations
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for j in range(n):
        if j % 2 == 0:
            ans += arr[j]

    arr1 = []
    for j in range(1, n, 2):
        arr1.append(arr[j] - arr[j - 1])

    msf = 0
    meh = 0
    for j in range(len(arr1)):
        meh += arr1[j]
        if msf <= meh:
            msf = meh
        if meh < 0:
            meh = 0
    cur1 = ans + msf

    arr2 = []
    for j in range(2, n, 2):
        arr2.append(arr[j - 1] - arr[j])

    msf = 0
    meh = 0
    for j in range(len(arr2)):
        meh += arr2[j]
        if msf <= meh:
            msf = meh
        if meh < 0:
            meh = 0
    cur2 = ans + msf
    print(max(cur1, cur2))
