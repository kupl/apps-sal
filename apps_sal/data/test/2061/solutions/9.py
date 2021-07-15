
def make_set(a):
    parent[a] = a
    size[a] = 1
    
      
def find_set(a):
        if a == parent[a]:
            return a
        else:
            parent[a] = find_set(parent[a])
        return parent[a]
    

def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        
        
        
        
def is_valid(a):
    i = a[0]
    j = a[1]
    if 0<=i<=n-1 and 0<=j<=m-1:
        if A[i][j] == '.':
            if (i,j) not in parent:
                return False
            else:
                return True 
        else:
            return True
    else:
        return True
        
        
        
        
        
parent = dict()
size = dict()
n,m,ks = map(int, input().split())
A = [0] * n
for i in range(n):
    A[i] = list(input())

for i in range(n):
    for j in range(m):
        if i != 0 and j != 0 and i != n - 1 and j != m - 1:
        
            if A[i][j] == '.':
                if is_valid((i-1,j)) and is_valid((i,j-1)):
                    
                    make_set((i,j))
                    if (i-1,j) in parent:
                        union_sets((i-1,j), (i,j))
                    if (i,j-1) in parent:
                        union_sets((i,j-1), (i,j))
                else:
                    if A[i][j] =='.':
                        dels = []
                        if (i-1,j) in parent:
                            a1 = find_set((i-1,j))
                           
                            for k in parent:
                                if find_set(k) == a1:
                                    
                                    dels.append(k)
                      
                        for f in dels:
                            
                            parent.pop(f)
                        dels = []
                        if (i,j-1) in parent:
                            
                            a1 = find_set((i,j-1))
                            
                            for k in parent:
                                if find_set(k) == a1:
                                    dels.append(k)
                        
                        for f in dels:
                            
                            parent.pop(f)            
                        
        else:
            if A[i][j] =='.':
                dels = []
                if (i-1,j) in parent:
                    a1 = find_set((i-1,j))
                   
                    for k in parent:
                        if find_set(k) == a1:
                            
                            dels.append(k)
              
                for f in dels:
                    
                    parent.pop(f)
                dels = []
                if (i,j-1) in parent:
                    
                    a1 = find_set((i,j-1))
                    
                    for k in parent:
                        if find_set(k) == a1:
                            dels.append(k)
                
                for f in dels:
                    
                    parent.pop(f)    

ans = 0
ass = 0
ans2 = []
for j in parent:
    a1 = find_set(j)
    if a1 not in ans2:
        ans2.append(a1)
        ans +=1
for j in range(ans-ks):
    mins = float('infinity')
    numer = 0
    new_sizes = dict()
    for t in parent:
        a1 = find_set(t)
        if a1 in new_sizes:
            new_sizes[a1] +=1
        else:
            new_sizes[a1] = 1
    
    for t in new_sizes:
        if new_sizes[t] < mins:
            mins = new_sizes[t]
            numer = t
    ass += mins 
    dels = []
    for t in parent:
        
        if find_set(t) == numer:
            dels.append(t)
            
            A[t[0]][t[1]] = '*'      
    for t in dels:
        parent.pop(t)
print(ass)
for j in range(n):
    print(''.join(A[j]))
