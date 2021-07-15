x=int(input())
ans=0
while True:
    if ans*(ans+1)/2 >= x:
        print(ans)
        break
    ans+=1

