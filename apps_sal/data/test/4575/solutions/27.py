import sys
n = int(input())
(d, x) = map(int, input().split())
a = [int(input()) for i in range(n)]
c = 0
for i in a:
    p = (d - 1) // i + 1
    c += p
print(c + x)
