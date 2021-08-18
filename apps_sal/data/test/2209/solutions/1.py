import sys

f = sys.stdin

n = int(f.readline())
s = [f.readline().strip() for _ in range(n)]
s = [(x, x.count('s'), x.count('h')) for x in s]
s = sorted(s, key=lambda x: x[2] / float(x[1] + 0.00000001))
s = ''.join(x[0] for x in s)

cs = 0
ans = 0
for x in s:
    if x == 's':
        cs += 1
    else:
        ans += cs
print(ans)
