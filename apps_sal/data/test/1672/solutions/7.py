import sys
n = int(sys.stdin.readline())
res = 0
d = 0
t = 0
for i in range(n):
    d = int(sys.stdin.readline())
    if t != d:
        res += 1
        t = d
print(res)
