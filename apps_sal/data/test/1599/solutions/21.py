from fileinput import *

data = []
for line in input():
    if lineno() == 1:
        s = line.strip()
    if lineno() == 2:
        m = int(line.strip())
    if lineno() >= 3 and lineno() < 3 + m:
        data += [list(map(int, line.split()))]

slen = len(s)
a = [0] * slen

count = 0
for i in range(1, slen):
    if s[i] == s[i-1]:
        count += 1
    a[i] = count

for [l, r] in data:
    ll = l - 1
    rr = r - 1
    print(a[rr]-a[ll])

