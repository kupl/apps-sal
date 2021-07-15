def solve(data, n, m):
    i = 1
    j = n
    flags1 = [False]*(n+1)
    flags2 = [False]*(n+1)
    for x in data:
        if flags1[x[0]] and flags1[x[1]]:
            return 0
        elif flags2[x[0]] and flags2[x[1]]:
            return 0
        else:
            if (x[0] > x[1]):
                flags1[x[0]] = True
                flags2[x[1]] = True
            else:
                flags2[x[0]] = True
                flags1[x[1]] = True
    while i<(n+1) and flags1[i]==False:
        i+=1
    while j>0 and flags2[j]==False:
        j-=1
    if (j==0):
        return n-1
    elif (i < j):
        return 0
    else:
        return i-j
        
numb = [int(x) for x in input().split()]
n = numb[0]
m = numb[1]
data = []
for k in range(m):
    data.append([int(x) for x in input().split()])
    
print(solve(data,n,m))
