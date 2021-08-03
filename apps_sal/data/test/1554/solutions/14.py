3

n = int(input())
a = [int(x) for x in input().split()]

r = []
s = set()
l = 0
for i, x in enumerate(a):
    if x in s:
        r.append([l + 1, i + 1])
        l = i + 1
        s = set()
    else:
        s.add(x)
if l == 0:
    print(-1)
else:
    if s:
        r[-1][1] = n
    print(len(r))
    print('\n'.join('{0} {1}'.format(p, q) for (p, q) in r))
