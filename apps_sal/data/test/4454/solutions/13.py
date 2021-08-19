# import sys
# sys.stdin = open("in.txt", "r")

t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    s = sum(arr)
    avg = s // n
    if avg * n < s:
        avg += 1
    print(avg)
