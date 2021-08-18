import math
import collections
def ii(): return int(input())


def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


s = input()
t = input()
n = len(s)

for i in range(n):
    flag = 0
    for j in range(n):
        if s[(i + j) % n] != t[j]:
            flag = 1
            break
    if flag == 0:
        print('Yes')
        return
print('No')
