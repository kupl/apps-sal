'''input
121 130
'''
from sys import stdin


l, r = list(map(int, stdin.readline().split()))
x = l
for i in range(l, r + 1):
    arr = list(str(i))
    if len(arr) == len(set(arr)):
        print(i)
        break
else:
    print(-1)
