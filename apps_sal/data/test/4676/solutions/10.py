import math
import collections
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


o = input()
e = input()
for i in range(len(e)):
    print(o[i] + e[i], end="")
if len(o) != len(e):
    print(o[-1])
else:
    print()
