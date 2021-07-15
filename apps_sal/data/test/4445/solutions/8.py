#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue
sys.setrecursionlimit(1000000)
#sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))
od = []
ev = []
for i in range(n):
    if a[i]%2 == 0: ev.append(a[i])
    else: od.append(a[i])
od.sort()
ev.sort()

if abs(len(od)-len(ev)) <= 1:
    print(0)
    return

ans = 0
if len(od) > len(ev):
    for i in range(len(od)-len(ev)-1):
        ans += od[i]
else:
    for i in range(len(ev)-len(od)-1):
        ans += ev[i]
print(ans)
