n=int(input())

#L=[n//i*(i+n//i*i)//2 for i in range(1,n+1)]
#print(sum(L))
ans=0
#for i in range(1,n+1):
#    for j in range(1,n+1):
#        if i%j==0:
#            ans+=i
#print(ans)
g=lambda x:(x*(n//x)*(n//x+1))//2
print((sum(g(i) for i in range(1,n+1))))

