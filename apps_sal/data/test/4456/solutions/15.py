# https://codeforces.com/contest/1213/problem/F

n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

def get(cur):
    if cur>=97+25:
        return chr(97+25)
    return chr(cur)

pos = [0] * (n+1)
for i, x in enumerate(q):
    pos[x] = i
    
seg =[0]
cnt = 0
max_=-1

for i, x in enumerate(p):
    max_ = max(max_, pos[x])    
    if i == max_:
        cnt+=1
        seg.append(i+1)
        
if len(seg)-1<k:
    print('NO')
else:
    cur = 97 
    S   = []
    for s, e in zip(seg[:-1], seg[1:]):
        for i in range(s, e):
            S.append(cur)
        cur+=1    
    
    print('YES')
    print(''.join([get(S[pos[x]]) for x in range(1, n+1)]))        
