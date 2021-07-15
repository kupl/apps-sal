#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue, bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9+7
sys.setrecursionlimit(1000000)

x = list(map(int, input().split()))
d = x.pop()
x.sort()
ans = 0
if x[1]-x[0] < d:
    ans += d-x[1]+x[0]
if x[2]-x[1] < d:
    ans += d-x[2]+x[1]
print(ans)
