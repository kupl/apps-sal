from operator import itemgetter
n, *ABCD = map(int, open(0).read().split())
AB = sorted([(a, b) for a, b in zip(ABCD[:2*n:2], ABCD[1:2*n:2])])
CD = sorted([(c, d) for c, d in zip(ABCD[2*n::2], ABCD[2*n+1::2])])

for c, d in CD:
    t_AB = [(a, b) for a, b in AB if a < c and b < d]
    if t_AB:
        t_AB.sort(key=itemgetter(1))
        AB.remove(t_AB[-1])
print(n-len(AB))
