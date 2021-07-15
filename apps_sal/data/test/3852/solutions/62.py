N = int(input())
a = list(map(int, input().split()))
m = 10**18
M = -10**18
m_idx = -1
M_idx = -1

for i in range(N):
    if a[i]<m:
        m = a[i]
        m_idx = i
    
    if a[i]>M:
        M = a[i]
        M_idx = i
        
ope = []

if abs(m)<=abs(M):
    for i in range(N):
        ope.append((M_idx, i))
    
    for i in range(N-1):
        ope.append((i, i+1))
else:
    for i in range(N):
        ope.append((m_idx, i))
    
    for i in range(N-1, 0, -1):
        ope.append((i, i-1))
    
print(len(ope))

for x, y in ope:
    print(x+1, y+1)
