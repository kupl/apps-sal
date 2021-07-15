t=int(input())
for you in range(t):
    n=int(input())
    l=input().split()
    li=[int(i) for i in l]
    lodd=[]
    leven=[]
    for i in li:
        if(i%2):
            lodd.append(i)
        else:
            leven.append(i)
    if(len(leven)%2==0):
        print("YES")
    else:
        done=0
        for i in lodd:
            for j in leven:
                if(abs(i-j)==1):
                    done=1
                    break
        if(done):
            print("YES")
        else:
            print("NO")

