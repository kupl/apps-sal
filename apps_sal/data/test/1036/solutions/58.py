from collections import defaultdict
(n, k) = list(map(int, input().split()))
s = input()
d = defaultdict(lambda: defaultdict(str))
(d['R']['R'], d['R']['S'], d['S']['R']) = ('R', 'R', 'R')
(d['P']['P'], d['P']['R'], d['R']['P']) = ('P', 'P', 'P')
(d['S']['S'], d['S']['P'], d['P']['S']) = ('S', 'S', 'S')
s2 = s + s
count = k
while count > 0:
    tmp = ''
    for i in range(0, len(s2), 2):
        tmp += d[s2[i]][s2[i + 1]]
    s2 = tmp + tmp
    count -= 1
print(s2[0])
