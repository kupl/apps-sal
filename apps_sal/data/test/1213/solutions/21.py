n,k=list(map(int,input().split()))

x=input()
t=min(n-k,k-1)

ans=""
if (n==1):
    ans="PRINT "+x

else:

    if (t==n-k):
        if (t==0):
            j=n-1
            while (j>0):
                ans+="PRINT "+x[j]+"\n"+"LEFT\n"
                j-=1

            ans+="PRINT "+x[0]+"\n"
        else:
            ans=t*"RIGHT\n"
            j=n-1
            while(j>0):
                ans+="PRINT "+x[j]+"\n"+"LEFT\n"
                j-=1

            ans+="PRINT "+x[0]+"\n"

    else:
        if (t==0):
            j=0
            while (j<n-1):
                ans+="PRINT "+x[j]+"\n"+"RIGHT\n"
                j+=1
            ans+="PRINT "+x[n-1]+"\n"
        else:
            ans=t*"LEFT\n"
            j=0
            while (j<n-1):
                ans+="PRINT "+x[j]+"\n"+"RIGHT\n"
                j+=1

            ans+="PRINT "+x[n-1]+"\n"

print (ans)
                
            
            

            
                
        
    

