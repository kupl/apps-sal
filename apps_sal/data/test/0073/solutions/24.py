import sys

input = sys.stdin.readline

c, v0, v1, a, l = map(int,input().split())

day = 0
read = 0

while True:
    if (read >= c):
        break
    if (v0 + a * day < v1):
        read += v0 + a * day
    else:
        read += v1
    if (day > 0):
        read -= l
    day += 1

print(day)
