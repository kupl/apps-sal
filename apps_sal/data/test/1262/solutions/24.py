import sys
#import heapq as hq
#from collections import deque
#sys.stdin = open('in', 'r')
readline = sys.stdin.readline
rdw = lambda: readline().rstrip()
rdws = lambda: readline().split()
rdwl = lambda: list(readline().split())
rdi = lambda: int(readline())
rdis = lambda: list(map(int, readline().split()))
rdil = lambda: list(map(int, readline().split()))
rdilrows = lambda cnt: [rdil() for _ in range(cnt)]

def solve():
    res = 0
    bld = []
    wire = []
    n = rdi()
    cities = rdilrows(n)
    c = rdil()
    p = [-1 for i in range(n)]
    k = rdil()
    used = set()
    used.add(-1)
    
    for i in range(n):
        cost, bst = min([(c[i], i) for i in range(n) if i not in used])
        par = p[bst]
        used.add(bst)
        res += cost
        if par == -1:
            bld.append(bst + 1)
        else:
            wire.append((bst + 1, par + 1))
        for j in range(n):
            if j not in used:
                wcost = (k[bst]+k[j])*(abs(cities[bst][0]-cities[j][0]) \
                                    + abs(cities[bst][1]-cities[j][1]))
                if wcost < c[j]:
                    c[j] = wcost
                    p[j] = bst
    
    sys.stdout.write(f'{res}\n')
    sys.stdout.write(f'{len(bld)}\n')
    sys.stdout.write(f'{" ".join(map(str, bld))}\n')
    sys.stdout.write(f'{len(wire)}\n')
    for i in range(len(wire)):
        sys.stdout.write(f'{wire[i][0]} {wire[i][1]}\n')


tests = 1
#tests = rdi()
for testnum in range(tests):
    solve()
    
#n = rdi()
#n,m = rdis()
#s = rdw()
#a = rdil()
#op, *s = rdws()

#print(f'Case #{testnum+1}: {res}')
#print(*res, sep='\n')
#sys.stdout.write('YES\n')
#sys.stdout.write(f'{res}\n')
#sys.stdout.write(f'{y1} {x1} {y2} {x2}\n')

