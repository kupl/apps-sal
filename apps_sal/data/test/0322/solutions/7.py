import sys

input = sys.stdin.readline

n = int(input())

neg = 0
pos = 0

for i in range(n):
    x,y = list(map(int,input().split()))
    if (x < 0):
        neg += 1
    else:
        pos += 1
    if (neg > 1 and pos > 1):
        print("No")
        return
print("Yes")

