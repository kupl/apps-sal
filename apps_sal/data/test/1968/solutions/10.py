from collections import OrderedDict
n, v = map(int, input().split())

pr = {}

for i in range(n):
    t = list(map(int, input().split()))[1:]
    pr[i+1]=min(t)

pr = OrderedDict(sorted(pr.items(), key=lambda x: x[1]))

k = 0

rr = []

for i in pr:
    if pr[i] < v:
        k += 1
        rr.append(i)

print(k)

rr.sort()

print(*rr, sep=' ')

