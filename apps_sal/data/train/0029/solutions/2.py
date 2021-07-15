import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    S = {}
    for el in arr:
        S[el] = [0]
        
    for i in range(len(arr)):
        S[arr[i]].append(i+1)
        
    G = {}
    
    for key in S:
        S[key].append(n+1)
        best = 0
        for i in range(len(S[key]) - 1):
            gap = abs(S[key][i] - S[key][i+1])
            best = max(gap, best)
        G[key] = best
        
    #print(G)
    B = {}
    for key in G:
        l = G[key]
        if l not in B:
            B[l] = key
        else:
            B[l] = min(B[l], key)
            
    ans = []
    for key in B:
        ans.append((key, B[key]))
        
    ans.sort()
    
    pp = []
    low = 9999999999999999
    j = 0
    for i in range(1, n+1):
        if j<len(ans) and i==ans[j][0]:
            if ans[j][1] < low:
                low = ans[j][1]
            j += 1
        if low > 10**10:
            pp.append(-1)
        else:
            pp.append(low)
            
    print(*pp)
        
        

