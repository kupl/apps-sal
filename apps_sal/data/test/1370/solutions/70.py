import itertools
H, W, K = map(int,input().split())
S = [list(map(int,list(input()))) for _ in range(H)]
def check(k):
    if k <= K:
        return(True)
    else:
        return(False)
        
noans = 0
def make_lst(i):
    nonlocal noans, lst, havelst
    temp = S[0][i]
    for h in range(H-1):
        if y[h]:
            lst.append(temp)
            temp = S[h+1][i]
        else:
            temp += S[h+1][i]
    lst.append(temp)
    if check(max(lst)):
        havelst = 1
    else:
        noans = 1
#    print(y,i,lst, "makelst")
               
def nocut(i):
    nonlocal cutnum, lst, havelst, noans
    prelst = []
    temp = S[0][i]
    if i == W-1:
        if not check(temp):
            noans = 1
    j = 0
    for h in range(H-1):            
        if y[h]:
            lst[j] += temp
            prelst.append(temp)
            j += 1
            temp = S[h+1][i]
        else:
            temp += S[h+1][i]
        if i == W-1:
            if not check(temp):
                noans = 1
    prelst.append(temp)
    lst[-1] += temp
    if check(max(lst)):
#        print(y,i,lst,"nocut", "cutnum = ",cutnum)
        return(True)
    else:
        cutnum += 1
        lst = prelst        
#        print(y,i,lst,"cut","cutnum =",cutnum)
        
                 
ans = float("inf")    
for y in itertools.product((0, 1), repeat=H-1):
    havelst = 0
    lst = []
    cutnum = sum(y)
    for x in range(W):
        if noans:
            break
        if havelst:
            nocut(x)
        else:
            make_lst(x)
#    print(y,cutnum)
    if noans:
        noans = 0
        continue
    else:
        ans = min(cutnum, ans)
print(ans)
