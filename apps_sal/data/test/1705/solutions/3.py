import sys

input = sys.stdin.readline

n = int(input())

last0 = -1
last1 = -1

a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] == 1:
        last1 = i
    else:
        last0 = i

print(min(last0, last1) + 1)
