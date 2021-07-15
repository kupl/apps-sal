import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
v = True
if 2 * max(a) > sum(a):
    v = False
if sum(a) % 2 == 1:
    v = False
if v == True:
    print("YES")
else:
    print("NO")
