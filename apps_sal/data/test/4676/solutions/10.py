import math
import collections
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

o = input()
e = input()
for i in range(len(e)):
    print(o[i] + e[i], end="")
if len(o) != len(e):
    print(o[-1])
else:
    print()
