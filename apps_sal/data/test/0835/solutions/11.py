s = input()
(nb, ns, nc) = map(int, input().split())
(pb, ps, pc) = map(int, input().split())
r = int(input())
d = {'B': 0, 'S': 0, 'C': 0}
for c in s:
    d[c] += 1
(db, ds, dc) = (d['B'], d['S'], d['C'])


def f(x):
    return max(0, x * db - nb) * pb + max(0, x * ds - ns) * ps + max(0, x * dc - nc) * pc


(a, b) = (0, 1000000001000)
while a < b:
    m = (a + b) // 2
    if f(m) < r:
        a = m + 1
    elif f(m) > r:
        b = m - 1
    else:
        a = m
        break
if f(a) > r:
    a -= 1
print(a)
