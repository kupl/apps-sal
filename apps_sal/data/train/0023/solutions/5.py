import sys
import heapq
 
 
def solve(pr, mm):
    omm = []
    n = len(mm)
    for i in range(n + 1):
        omm.append([])
    
    for i in range(n):
        omm[mm[i]].append(pr[i])
    
    for i in range(n + 1):
        omm[i] = sorted(omm[i])
    
    heap = []
    c = 0
    t = n
    p = 0
    for i in range(n, -1, -1):
        for h in omm[i]:
            heapq.heappush(heap, h)
            
        t -= len(omm[i])
        mn = max(i - c - t, 0)
        c += mn
        for j in range(mn):
            p += heapq.heappop(heap)
        
    return p
    
 
def __starting_point():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        ms = []
        ps = []
        for j in range(n):
            arr = [int(v) for v in input().strip().split(' ')]
            ms.append(arr[0])
            ps.append(arr[1])
            
        print(solve(ps, ms))

__starting_point()
