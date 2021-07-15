n=int(input())
l=list(map(int,input().split()))
L=[[0,1]]
for i in range(1,n) :
    v=L[i-1][1]+1
    L.append([v,0])
    y=L[l[i]-1][0]
    L[i][1]=v+v-y+1
    
print((L[-1][1]+1)%1000000007)

