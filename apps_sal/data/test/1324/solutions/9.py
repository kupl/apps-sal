import sys

f = sys.stdin
a = [int(u) for u in f.readline().strip().split()]

s = f.readline().strip()

res = 0
for u in s:
    res += a[int(u)-1]

print(res)    

