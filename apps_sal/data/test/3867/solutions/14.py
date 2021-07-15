from collections import Counter,defaultdict,deque

read = lambda : list(map(int,input().split()))
getinfo = lambda grid: print(list(map(print,grid)))
p = lambda x: print(x,end=" ")

mod = 10**9 + 7
inf = float('inf')

def solve(a):
    if a[0] != 1: return 'No'
    index = 1
    d1 = defaultdict(set)
    for i in range(n):
        for j in range(index, index+len(d[a[i]])):
            d1[a[i]].add(a[j])
            d[a[j]].discard(a[i])
        if d1[a[i]] != d[a[i]]: return 'No'
        index += len(d[a[i]])
    return 'Yes'

n = int(input())
d = defaultdict(set)
for i in range(n-1):
    a,b = read()
    d[a].add(b)
    d[b].add(a)
a = read()
print(solve(a))

