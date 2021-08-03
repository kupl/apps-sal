from sys import stdin

input = stdin.readline

n = int(input())
s = [0] + [int(item) for item in input().split(' ')]
pre = s[0]

q = int(input())
x = {}
lowest = s[1]
while q:
    [w, h] = [int(item) for item in input().split(' ')]
    height = max(lowest, s[w])
    lowest = height + h
    print(height)
    q -= 1
