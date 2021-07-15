n=int(input())
m=list()
for i in range (n):
    m.append(input())
    
for i in range(n):
    for j in range(n):
        k=0
        if (i>0) and (m[i-1][j]=='o'):
            k+=1
        if (i<(n-1)) and (m[i+1][j]=='o'):
            k+=1
        if (j>0) and (m[i][j-1]=='o'):
            k+=1
        if (j<n-1) and (m[i][j+1]=='o'):
            k+=1
        if (k%2):
            print("NO")
            return
print("YES")
