n=int(input())
ans=[]
if n==0:
    print(0)
    return
while True:
    if n==0:
        break
    if n>=0:
        ans.append(n%2)
        n=(-1)*(n//2)
    else:
        ans.append((n*-1)%2)
        if (n*-1)%2==1:
            n=(n*-1)//2+1
        else:
            n=(n*-1)//2
    

for i in range(len(ans)):
    ans[i]=str(ans[i])
print("".join(list(ans[::-1])))
