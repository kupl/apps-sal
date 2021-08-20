(s, K) = open(0).read().split()
K = int(K)
ss = set()
temp = set([''])
for x in s:
    temp = set([''.join((y, x)) for y in temp if len(y) <= 4])
    ss = ss | temp
    temp.add('')
l = list(ss)
l.sort()
print(l[K - 1])
