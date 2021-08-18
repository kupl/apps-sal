import sys

reader = (list(map(int, line.split())) for line in sys.stdin)
input = reader.__next__

t, = input()
for _ in range(t):
    n, m = input()
    a = list(input())
    b = list(input())
    d = {el: i for i, el in enumerate(a)}
    maxPos = d[b[0]]
    ans = 2 * maxPos + 1
    Nremoved = 1
    for el in b[1:]:
        pos = d[el]
        if pos < maxPos:
            ans += 1
        else:
            ans += 2 * (pos - Nremoved) + 1
            maxPos = pos
        Nremoved += 1
    print(ans)
