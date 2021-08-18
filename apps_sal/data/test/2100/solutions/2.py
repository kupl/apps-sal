import sys
f = sys.stdin
f.readline()
l, r = [], []
res = 0
for line in f:
    l += line.strip().split()[0]
    r += line.strip().split()[1]
if l.count('0') < l.count('1'):
    res += l.count('0')
else:
    res += l.count('1')
if r.count('0') < r.count('1'):
    res += r.count('0')
else:
    res += r.count('1')
print(res)
