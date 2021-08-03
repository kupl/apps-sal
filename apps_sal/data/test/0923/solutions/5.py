import sys
sys.setrecursionlimit(1000000000)

n = int(input())
s = input().split()
t = []
for i in range(n):
    t += [int(s[i])]
x = 0
if t[0] != 0:
    x = n - t[0]
bb = True
for i in range(n):
    if i % 2 == 0 and (t[i] + x) % n != i:
        bb = False
    if i % 2 == 1 and (t[i] - x) % n != i:
        bb = False
if bb:
    print("Yes")
else:
    print("No")
