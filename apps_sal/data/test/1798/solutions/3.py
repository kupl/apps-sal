3

def readln(): return tuple(map(int, input().split()))

n, = readln()
var = {}
for i, a in enumerate(readln()):
    if a in var:
        var[a].append(i)
    else:
        var[a] = [i]
ans = []
for x, v in list(var.items()):
    if len(v) == 1:
        ans.append((x, 0))
    else:
        d = set([v[i] - v[i - 1] for i in range(1, len(v))])
        if len(d) == 1:
            ans.append((x, d.pop()))
print(len(ans))
print('\n'.join('%d %d' % f for f in sorted(ans)))

