X,Y,Z,K= list(map(int,input().split()))
l_A=list(map(int,input().split()))
l_B=list(map(int,input().split()))
l_C=list(map(int,input().split()))
l_A.sort(reverse=True)
l_B.sort(reverse=True)
l_C.sort(reverse=True)
l=[]
for i in range(len(l_A)):
   for j in range(len(l_B)):
      for k in range(len(l_C)):
        if (i+1)*(j+1)*(k+1) > K:
           break
        l+=[l_A[i]+l_B[j]+l_C[k]]
ans=sorted(l,reverse=True)[:K]
print(*ans,sep="\n")
