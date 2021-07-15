n = int(input())
segs = []

for i in range(n):
    segs.append(tuple(map(int, input().split())))

top3 = [ (0, 10**10), (0, 10**10), (0, 10**10) ]
every = (0, 10**10)


def inter(one, two):
    l1, r1 = one
    l2, r2 = two
    return max(l1,l2), min(r1,r2)

for i in segs:
    tp1 = inter(i, top3[0])
    tp2 = inter(i, top3[1])
    tp3 = inter(i, top3[2])
    tp4 = every
    every = inter(i, every)
    ntop3 = sorted([tp1, tp2, tp3, tp4], reverse=True, key=lambda x:x[1]-x[0])
    top3 = ntop3[:3]

res = sorted(top3, key=lambda x:x[1]-x[0])[-1]
print(max(res[1]-res[0], 0))


