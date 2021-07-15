n = int(input())
import sys
l = [0]+list(map(int,sys.stdin.readline().strip().split()))
x = 0
b = 0
m = int(input())
for _ in range(m):
    w,h = map(int,sys.stdin.readline().strip().split())
    x = max(x+b,l[w])
    b = h
    print(x)
