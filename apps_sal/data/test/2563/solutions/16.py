import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None]*T

for qu in range(T):
    S = list(map(ord, readline().strip()))
    
    SE = []
    SO = []
    
    for s in S:
        if s % 2 == 0:
            SE.append(s)
        else:
            SO.append(s)
    
    LE = len(SE)
    LO = len(SO)
    inf = 10000
    SE.append(inf)
    SO.append(inf)
    cnte = 0
    cnto = 0
    ans = []
    for _ in range(LE + LO):
        if SE[cnte] < SO[cnto]:
            ans.append(SE[cnte])
            cnte += 1
        else:
            ans.append(SO[cnto])
            cnto += 1
    
    Ans[qu] = ans

for a in Ans:
    sys.stdout.write(''.join(map(chr, a)))
    sys.stdout.write('\n')

