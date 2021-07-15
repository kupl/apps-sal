n, k = list(map(int, input().split()))
p  = {}
np = {}
pair    = []
used    = {}
rev_d   = {}

def push(d, s, v):
    if s not in d:
        d[s] = []
    d[s].append(v)

def is_pal(s):
    n = len(s)
    flg=True
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            flg = False
            break
    return flg        

def rev(s):
    return s[::-1]

for _ in range(n):
    s, val = input().split()
    val    = int(val)
    
    if is_pal(s):
        push(p, s, val)
    else:
        push(np, s, val)
        
        if s not in rev_d:
            rev_d[s] = rev(s)

for k, v in list(p.items()):
    p[k] = sorted(v, reverse=True)
        
for k, v in list(np.items()):
    np[k] = sorted(v, reverse=True)
    
for s in np:
    if s not in used and rev_d[s] in np:
        pair.append([s, rev_d[s]])
        used[s] = True
        used[rev_d[s]] = True
        
max_remain = 0
minus = 0
max_S = 0

for v_arr in list(p.values()):
    n = len(v_arr)
    for i in range(0, n, 2):
        if i+1==n:
            if v_arr[i] > 0:
                max_remain = max(max_remain, v_arr[i]) 
            
        else:
            if v_arr[i] + v_arr[i+1] >= 0:
                max_S += v_arr[i] + v_arr[i+1]
                
                if v_arr[i+1] < 0:
                    minus = min(minus, v_arr[i+1])
            else:
                if v_arr[i] > 0:
                    max_remain = max(max_remain, v_arr[i]) 

for [u, v] in pair:
    n = min(len(np[u]), len(np[v]))
        
    for x, y in  zip(np[u][:n], np[v][:n]):
        if x+y > 0:
            max_S += x+y
            
print(max(max_S+max_remain, max_S-minus))            

#7 3
#abb 2
#aaa -3
#bba -1
#zyz -4
#abb 5
#aaa 7
#xyx 4

