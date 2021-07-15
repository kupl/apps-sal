n = int(input())
s = list(input())

dg = 10**6
for i in range(n):
    s[i] = ord(s[i])*dg + i
s.sort()

def init_max(init_max_val):
    #set_val
    for i in range(n):
        seg_max[i+num_max-1]=init_max_val[i]    
    #built
    for i in range(num_max-2,-1,-1) :
        seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2]) 
    
def update_max(k,x):
    k += num_max-1
    seg_max[k] = x
    while k:
        k = (k-1)//2
        seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])
    
def query_max(p,q):
    if q<=p:
        return ide_ele_max
    p += num_max-1
    q += num_max-2
    res=ide_ele_max
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg_max[p])
        if q&1 == 1:
            res = max(res,seg_max[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg_max[p])
    else:
        res = max(max(res,seg_max[p]),seg_max[q])
    return res

ide_ele_max = 0

num_max =2**(n-1).bit_length()
seg_max=[ide_ele_max]*2*num_max


res = [0]*n
for e in s:
    ind = e%dg
    ad = query_max(ind,n)
    res[ind] = ad+1

    update_max(ind,ad+1)
print(max(res))
print(*res)
