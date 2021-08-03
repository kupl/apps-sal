import sys
from math import ceil

input = sys.stdin.readline

n = int(input())
a = map(int, input().split())

countPos = 0
countNeg = 0

for i in a:
    if i > 0:
        countPos += 1
    if i < 0:
        countNeg += 1

if countPos >= ceil(n / 2):
    print(1)
elif countNeg >= ceil(n / 2):
    print(-1)
else:
    print(0)
