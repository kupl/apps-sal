# https://codeforces.com/contest/1228/problem/D
# all neightbor in group --> pass 1
# all neighbor not in group --> merge 0
# invalid 2
# WA
def type_(list_v, group):
    cnt_0 = 0
    cnt_1 = 0
    
    for v in list_v:
        if v in group:
            cnt_1 += 1
        else:
            cnt_0 += 1
            
    if cnt_1 == len(group):
        return 1
    
    if cnt_0 == len(list_v):
        return 0
    
    return 2
    
def is_all_type_1(ex_index, list_group, v):
    for i, group in list(list_group.items()):
        if i == ex_index:
            continue
            
        if type_(g[v], group) != 1: 
            return False
        
    return True
    
def check(v, list_group):
    t = None
    for i, group in list(list_group.items()):
        t  = type_(g[v], group)
        
        if t == 0 or t == 2:
            if t == 0:
                if is_all_type_1(i, list_group, v) == True:
                    group[v] = 1
                else:
                    return 2
            return t
        
    return t    
    
group = {}    
def process(g):    
    for v in g:
        if len(group) == 0:
            group[0]    = {}
            group[0][v] = 1
            continue
    
        t = check(v, group)
        
        if t == 2:
            return -1
        
        if t == 1:
            if len(group) == 3:
                return -1
            
            group[len(group)]    = {}
            group[len(group)-1][v] = 1
    return group

g = {}
n, m = list(map(int, input().split()))

for _ in range(m):
    u, v = list(map(int, input().split()))
    if u not in g:
        g[u] = []
    if v not in g:
        g[v] = []
        
    g[u].append(v)    
    g[v].append(u)
    
ans = process(g)

if ans == -1 or len(ans) < 3:
    print(-1)
else:
    pr  = [0] * n
    
    cnt = 0
    for k, gr in list(group.items()):
        for v in gr:
            cnt += 1
            pr[v-1] = str(k+1)
    
    if cnt == n:
        print(' '.join(pr))
    else:
        print(-1)
# 1,2  3,4  5,6
#6 12
#1 3
#1 4
#2 3
#2 4
#1 5 
#1 6
#2 5
#2 6
#3 5
#3 6
#4 5
#4 6

