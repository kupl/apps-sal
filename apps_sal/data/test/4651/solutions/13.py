for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    stack=[]
    marked={}
    i=0
    j=1
    result=[]
    while j<=n:
        if j not in marked:
            stack=[]
            result.append(j)
            while l1[i]!=j:
                marked[l1[i]]=1
                stack.append(l1[i])
                i+=1
            marked[j]=1

            if stack:
                l1[i]=stack[-1]
                del marked[stack[-1]]
                result.extend(stack[:len(stack)-1])
            else :
                i+=1
        j+=1
    print(*result,sep=" ")
            
