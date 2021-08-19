(n, k) = map(int, input().split())
s = list(input())
d = dict()
(d['R', 'S'], d['S', 'R']) = ('R', 'R')
(d['P', 'R'], d['R', 'P']) = ('P', 'P')
(d['S', 'P'], d['P', 'S']) = ('S', 'S')
(d['R', 'R'], d['P', 'P'], d['S', 'S']) = ('R', 'P', 'S')
t = s + s
for _ in range(k):
    for i in range(n):
        t[i] = d[t[2 * i], t[2 * i + 1]]
    for i in range(n):
        t[n + i] = t[i]
ans = t[0]
print(ans)
