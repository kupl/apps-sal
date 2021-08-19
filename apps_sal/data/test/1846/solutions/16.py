import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
t = list(map(int, input().split()))
l = []
r = [0] * (n - 1)
p = m = 0
for i in range(n - 1):
    if t[i] > -1:
        p += 1
    l.append(p)
for i in range(n - 1, 0, -1):
    if t[i] < 1:
        m += 1
    r[i - 1] = m
mn = float('+inf')
for i in range(n - 1):
    mn = min(mn, l[i] + r[i])
print(mn)
