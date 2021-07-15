# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

#n = int(readline())
h,w = list(map(int,readline().split()))
s = read().split()


good_move = [[None]*h for _ in range(h)]
for i in range(h):
    for j in range(i,h):
        se = set()
        for p in range(w):
            for q in range(p,w):
                if s[i][p] == s[j][q] and s[i][q] == s[j][p]:
                    se.add(p*16+q)
        good_move[i][j] = se

#print(good_move)
        
def check(q):
    def isok(x,y):
        return all(x*16+y in good_move[r[2*i]][r[2*i+1]] for i in range((h+1)//2))
    
    def dfs2(d,p):
        if d == w:
            return True
        
        if d==0 and w&1:
            for idx in range(w):
                if isok(idx,idx):
                    p[idx] = 0
                    if dfs2(1,p): return True
                    p[idx] = -1
            return False

        idx = p.index(-1)
        #print(p,idx)
        p[idx] = d
        for k in range(idx+1,w):
            #print(idx,k,idx*16+k,isok(idx,k))
            if p[k] == -1 and isok(idx,k):
                p[k] = d+1
                if dfs2(d+2,p): return True
                p[k] = -1
        p[idx] = -1
        return False
    
    r = [0]*h
    for i in range(h):
        r[q[i]] = i
    if h&1:
        r.append(r[-1])
    #print(r); return False
    p = [-1]*w
    return dfs2(0,p)

def dfs(d):
    #nonlocal cnt
    nonlocal flag
    if d == h or d == h-1:
        #cnt += 1;return False
        return check(p)

    if d==0 and h&1 and flag:
        flag = 0
        for idx in range(h):
            p[idx] = h-1
            if dfs(0): return True
            p[idx] = -1
        return False
    
    #print(p,d)
    idx = p.index(-1)
    p[idx] = d
    for k in range(idx+1,h):
        if p[k] == -1:
            p[k] = d+1
            if dfs(d+2): return True
            p[k] = -1
    p[idx] = -1
    return False

p = [-1]*h
cnt = 0
flag = 1
if dfs(0):
    print("YES")
else:
    print("NO")
#print(cnt)

