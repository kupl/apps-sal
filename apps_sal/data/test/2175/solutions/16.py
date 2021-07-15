'''
Created on 2016-4-9

@author: chronocorax
'''

def line():
    return [int(c) for c in input().split()]

n = line()[0]
cap = line()
cap0 = cap[:]
nxt = [i + 1 for i in range(n)]

result = []

m = line()[0]
for _ in range(m):
    tup = line()
    if tup[0] == 1:
        p = tup[1] - 1
        p0 = p
        x = tup[2]
#         flush(p - 1, x)
        marker = []
        while p < n and cap[p] < x:
            x -= cap[p]
            cap[p] = 0
            marker.append(p)
            p = nxt[p]
        if p < n: cap[p] -= x
        for i in marker:
            nxt[i] = p
    else:
        k = tup[1]
        result.append(cap0[k - 1] - cap[k - 1])
    
for res in result:
    print(res)
