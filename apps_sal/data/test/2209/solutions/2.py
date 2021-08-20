import sys
f = sys.stdin
ans = 0
od = 0
n = int(f.readline())
s = [f.readline().strip() for _ in range(n)]
s = [(x, x.count('s'), x.count('h')) for x in s]
s = sorted(s, key=lambda x: x[2] / float(x[1] + 1e-07))
s = ''.join((x[0] for x in s))
for x in s:
    if x == 's':
        od += 1
    else:
        ans += od
print(ans)
