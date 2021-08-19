from collections import Counter
import sys
input = sys.stdin.readline
Q = int(input())
for testcases in range(Q):
    (n, k) = list(map(int, input().split()))
    if k % 3 != 0:
        if n % 3 == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        l = n % (k + 1)
        if l == k:
            print('Alice')
        elif l % 3 == 0:
            print('Bob')
        else:
            print('Alice')
