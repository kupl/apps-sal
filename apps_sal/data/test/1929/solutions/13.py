import sys

f = sys.stdin
n, t, c = list(map(int,f.readline().split()))

s = f.readline().split()

total = 0
r = 0 # длинна отрезка
for j in s:
    d = int(j)
    if (d<=t):
        r += 1
    else :
        if r>=c: total += r-c+1
        r = 0

if r>=c: total += r-c+1

print(str(total))    

