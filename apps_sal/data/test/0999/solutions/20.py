import sys
n = int(input())
min = sys.maxsize
max1 = 0
for _ in range(n):
    a, b = map(int, input().split())
    if min > b:
        min = b
    if max1 < a:
        max1 = a
m = int(input())
max = 0
min1 = sys.maxsize
for _ in range(m):
    a, b = map(int, input().split())
    if max < a:
        max = a
    if min1 > b:
        min1 = b
if max <= min:
    ans = 0
else:
    ans = max - min
if max1 <= min1:
    ans1 = 0
else:
    ans1 = max1 - min1
if ans > ans1:
    print(ans)
else:
    print(ans1)
