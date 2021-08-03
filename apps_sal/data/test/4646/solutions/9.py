from math import floor, ceil, pi
from collections import Counter, defaultdict

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(s, b):
    res = ""
    while s:
        res += BS[s % b]
        s //= b
    return res[::-1] or "0"


alpha = "abcdefghijklmnopqrstuvwxyz"

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    oddWrong = 0
    evenWrong = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            if arr[i] % 2 == 1:
                evenWrong += 1
        else:
            if arr[i] % 2 == 0:
                oddWrong += 1

    if oddWrong == evenWrong:
        print(oddWrong)
    else:
        print(-1)
