import itertools
n = int(input())
a = list(map(int, input().split()))
a = [(a[0], 1)] + sorted(zip(a[1:], itertools.count(2)), reverse=True)
w = 1
ans = []
for (r, cur) in enumerate(a):
    if r == w:
        print(-1)
        break
    while w != n and cur[0] > 0:
        ans.append('%s %s' % (cur[1], a[w][1]))
        cur = (cur[0] - 1, cur[1])
        w += 1
else:
    print(len(ans))
    print('\n'.join(ans))
