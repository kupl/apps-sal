from collections import defaultdict
(n, k) = list(map(int, input().split()))
s = input()
sL = []
for i in s:
    sL.append(i)
d = defaultdict(lambda: defaultdict(str))
(d['R']['S'], d['R']['R'], d['S']['R']) = ('R', 'R', 'R')
(d['P']['R'], d['P']['P'], d['R']['P']) = ('P', 'P', 'P')
(d['S']['P'], d['S']['S'], d['P']['S']) = ('S', 'S', 'S')
for _ in range(k):
    t = ''.join(sL + sL)
    for j in range(n):
        sL[j] = d[t[2 * j]][t[2 * j + 1]]
print(sL[0])
