from collections import defaultdict
(N, M) = map(int, input().split())
wa = defaultdict(int)
ac = {}
for i in range(M):
    (p, S) = input().split()
    if S == 'AC':
        ac[p] = True
    elif p not in ac:
        wa[p] += 1
print(len(ac), sum([wa[x] for x in ac.keys()]))
