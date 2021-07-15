import sys

n, m = map(int, input().split())
a = input().split()
b = input().split()
for _ in range(int(input())):
    y = int(input())
    y -= 1
    print(a[y % n] + b[y % m])
