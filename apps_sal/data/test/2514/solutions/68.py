import collections
n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = []
c = []
for i in range(q):
    (bi, ci) = list(map(int, input().split()))
    b.append(bi)
    c.append(ci)
count = collections.Counter(a)
sums = sum(a)
for i in range(q):
    sums += count[b[i]] * (c[i] - b[i])
    print(sums)
    count[c[i]] += count[b[i]]
    count[b[i]] = 0
