import sys

from collections import deque
# 26 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
input = lambda: sys.stdin.readline().strip()
ipnut = input
q = int(input())
for i in range(q):
    # n = int(input())
    h, n, m = list(map(int, input().split()))
    # a = list(map(int,input().split()))
    while n and h > 20:
        h = h // 2 + 10
        n -= 1
    while m and h > 0:
        h -= 10
        m -= 1
    if h > 0:
        print('NO')
    else:
        print("YES")
