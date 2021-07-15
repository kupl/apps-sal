import sys

t = int(input())
for i in range(t):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    print((a+b+c)//2)

