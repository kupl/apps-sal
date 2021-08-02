__autor__ = 'Esfandiar'
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
M = -float('inf')
for i in range(m):
    w, h = list(map(int, input().split()))
    if a[w - 1] < M:
        print(M)
        M += h
    else:
        print(a[w - 1])
        a[w - 1] += h
        M = a[w - 1]
