from collections import defaultdict as dd, deque

n = int(input())

V = [i+1 for i in range(n)]
E = dd(list)

for i in V[1:]:
    p = int(input())
    E[p].append(i)

for v in V:
    if len(E[v]) != 0 and sum(len(E[u])==0 for u in E[v]) < 3:
        print('No')
        break
else:
    print('Yes')

