n = int(input())
hs = tuple(int(x) for x in input().split())

def blocks(seq):
    res = 0
    i = 0 
    maxh = 0
    while True:
        if i == len(seq):
            return res
        maxh = max(maxh, seq[i])
        if maxh == i:
            res += 1
            i += 1 
        elif maxh > i:
            i += 1
            
def solve(n, hs):
    hhs = sorted((hs[i], i) for i in range(n))
    hhhs = sorted((i, hhs[i][0], hhs[i][1]) for i in range(n))
    return blocks(list(h[2] for h in hhhs)) 
    
print(solve(n, hs))

