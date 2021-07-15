# https://codeforces.com/problemset/problem/911/E

n, k = map(int, input().split())
p    = list(map(int, input().split()))
d    = {x:1 for x in p}

def solve(p, d, n):
    add  = []
    s    = []
    
    for x in range(1, n+1):
        if x not in d:
            while len(p) > 0:
                s.append(p.pop(0))
                
                if len(s) >= 2 and s[-1] > s[-2]:
                    return False, None
                
            # len(p)=0
            if len(s) == 0 or s[-1] != x:
                up = n if len(s) == 0 else s[-1]-1
            
                for y in range(up, x-1, -1):
                    add.append(y)
                    s.append(y)
                    d[y]=1
            s.pop()
        else:
            if len(s) == 0 or s[-1] != x:
                while len(p) > 0:
                    s.append(p.pop(0))
                
                    if len(s) >= 2 and s[-1] > s[-2]:
                        return False, None
                
                    if s[-1] == x:
                        break
            s.pop()
    return True, add

ans =  [x for x in p]
flg, add = solve(p, d, n)
if flg==False:
    print(-1)
else:
    print(' '.join([str(x) for x in ans+add]))
