def alldone(l):
    for i in l:
        if(i==0):
            return 0
    return 1
t=int(input())
for you in range(t):
    s=input()
    freq=[0 for i in range(26)]
    done=[0 for i in range(26)]
    for i in s:
        freq[ord(i)-97]+=1
    n=int(input())
    l=input().split()
    li=[int(i) for i in l]
    fist=[0 for i in range(n)]
    lfi=[]
    l=[]

    donefors=[0 for i in range(n)]
    for i in range(n):
        if(li[i]==0):
            l.append(i)
            donefors[i]=1
            lfi.append(i)
    for i in range(25,-1,-1):
        if(freq[i]>=len(l) and done[i]==0):
            done[i]=1
            for j in l:
                fist[j]=chr(97+i)
            l=[]
            break
        else:
            done[i]=1
    while(alldone(donefors)==0):
        for i in range(n):
            if(donefors[i]==1):
                continue
            else:
                z=li[i]
                for j in lfi:
                    li[i]=li[i]-abs(i-j)
                if(li[i]==0):
                    continue
                li[i]=z
        for i in range(n):
            if(li[i]==0 and donefors[i]==0):
                l.append(i)
                donefors[i]=1
        for i in l:
            lfi.append(i)


        for i in range(25,-1,-1):
            if(freq[i]>=len(l) and done[i]==0):
                done[i]=1
                for j in l:
                    fist[j]=chr(97+i)
                l=[]
                break
            else:
                done[i]=1
    for i in fist:
        print(i,end="")
    print()
