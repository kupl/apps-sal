from sys import stdin, stdout


n = int(stdin.readline())
challengers = []

for i in range(n):
    s = stdin.readline().strip().split()
    challengers.append((int(s[0]), s[1]))

challengers.sort()
G = []
R = []
B = []

for i in range(n):
    v = challengers[i]
    if v[1] == 'G':
        G.append(i)
    elif v[1]  == 'R':
        R.append(i)
    else:
        B.append(i)


test = []
for v in challengers:
    test.append(v[0])

challengers = test[:]

ans = 0

if len(G):
    indr, indb = 0, 0
    
    for i in range(len(G) - 1):
        while indr < len(R) and R[indr] < G[i]:
            indr += 1
        
        while indb < len(B) and B[indb] < G[i]:
            indb += 1
        
        mxr, mxb = 0, 0        
        
        previous = G[i]
        used1, used2 = 0, 0
        
        while indr < len(R) and R[indr] < G[i + 1]:
            mxr = max(mxr, challengers[R[indr]] - challengers[previous])
            previous = R[indr]
            indr += 1
            used1 = 1
    
        mxr = max(mxr, -challengers[previous] + challengers[G[i + 1]])
        
        previous = G[i]
        
        while indb < len(B) and B[indb] < G[i + 1]:
            mxb = max(mxb, challengers[B[indb]] - challengers[previous])
            previous = B[indb]
            indb += 1
            used2 = 1
    
        mxb = max(mxb, -challengers[previous] + challengers[G[i + 1]])

        
        d = challengers[G[i + 1]] - challengers[G[i]]
        ans += min(2 * d, 3 * d - mxb - mxr)
    
    
    if R and R[0] < G[0]:
        for i in range(1, len(R)):
            if R[i] > G[0]:
                ans += challengers[G[0]] - challengers[R[i - 1]]
                break
            else:
                ans += challengers[R[i]] - challengers[R[i - 1]]
        else:
            ans += challengers[G[0]] - challengers[R[-1]]
    
    if B and B[0] < G[0]:
        for i in range(1, len(B)):
            if B[i] > G[0]:
                ans += challengers[G[0]] - challengers[B[i - 1]]
                break
            else:
                ans += challengers[B[i]] - challengers[B[i - 1]]
        else:
            ans += challengers[G[0]] - challengers[B[-1]]
    
    
    label = 0
    
    if R and R[-1] > G[-1]:
        for i in range(len(R)):
            if not label and R[i] > G[-1]:
                ans += challengers[R[i]] - challengers[G[-1]]
                label = 1
            elif R[i] > G[-1]:
                ans += challengers[R[i]] - challengers[R[i - 1]]
            
            
    label = 0
    
    if B and B[-1] > G[-1]:
        for i in range(len(B)):
            if not label and B[i] > G[-1]:
                ans += challengers[B[i]] - challengers[G[-1]]
                label = 1
            elif B[i] > G[-1]:
                ans += challengers[B[i]] - challengers[B[i - 1]]    
else:
    for i in range(1, len(R)):
        ans += challengers[R[i]] - challengers[R[i - 1]]
    
    for i in range(1, len(B)):
        ans += challengers[B[i]] - challengers[B[i - 1]]

stdout.write(str(ans))


