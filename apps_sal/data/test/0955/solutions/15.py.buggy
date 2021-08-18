import collections
n = int(input())
l = collections.defaultdict(list)
x = []
f1, f2, f3 = 0, 0, 0
for i in range(n):
    c, s = input().split()
    c = int(c)
    s = ''.join(sorted(s))
    z = [i for i in s]
    if('A' in z):
        f1 = 1
    if('B' in z):
        f2 = 1
    if('C' in z):
        f3 = 1
    l[s].append(c)
    x.append(s)
if(not(f1 and f2 and f3)):
    print(-1)
    return
for i in x:
    l[i].sort()

t1, t2, t3, t4, t5, t6, t7, t8 = 10**9, 10**9, 10**9, 10**9, 10**9, 10**9, 10**9, 10**9
if(l['A'] and l['B'] and l['C']):
    t1 = l['A'][0] + l['B'][0] + l['C'][0]
if(l['AB'] and l['BC']):
    t2 = l['AB'][0] + l['BC'][0]
if(l['AB'] and l['AC']):
    t3 = l['AB'][0] + l['AC'][0]
if(l['AC'] and l['BC']):
    t4 = l['AC'][0] + l['BC'][0]
if(l['ABC']):
    t5 = l['ABC'][0]
if(l['A'] and l['BC']):
    t6 = l['A'][0] + l['BC'][0]
if(l['AC'] and l['B']):
    t7 = l['AC'][0] + l['B'][0]
if(l['AB'] and l['C']):
    t8 = l['AB'][0] + l['C'][0]
print(min(t1, t2, t3, t4, t5, t6, t7, t8))
