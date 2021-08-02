pops = int(input())
sa = [[0, 0] for t in range(pops)]
for t in range(pops):
    a, b = list(map(int, input().split(' ')))
    sa[t][0] = a
    sa[t][1] = b

sa.sort()

sa2 = [sa[x][1] for x in range(len(sa))]

sa3 = sa2[:]
sa2.sort()

if sa3 != sa2:
    print("Happy Alex")
else:
    print("Poor Alex")
