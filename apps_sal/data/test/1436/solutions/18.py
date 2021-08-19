import sys
f = sys.stdin
n = int(f.readline())
s = f.readline().split()
total = 0
r = 0
for j in s:
    d = int(j)
    if d < 0:
        if total == 0:
            r += 1
        else:
            total -= 1
    else:
        total += d
print(str(r))
