n=int(input())
p=list(map(int,input().split()))

icnt=0
i=0
while i<n:
    if p[i]==i+1:
        if i<n-1 and p[i+1]==i+2:
            icnt+=1
            i+=1
        else:
            icnt+=1            
    i+=1            

print(icnt)

