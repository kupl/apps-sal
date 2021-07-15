n=int(input())
a=input().split()
s=input()
if("1" not in s):
    print(0)
else:
    ls=[0 for i in range(n)]
    prefix=[0 for i in range(n)]
    valid=[0 for i in range(n)]
    for i in range(n):
        if(i==0):
            if(s[i]=="1"):
                ls[0]=int(a[i])
                valid[i]=1
            prefix[0]=int(a[i])
        else:
            if(s[i]=="1"):
                ls[i]=ls[i-1]+int(a[i])
                valid[i]=1
            else:
                ls[i]=ls[i-1]
            prefix[i]=prefix[i-1]+int(a[i])
    new_ls=[ls[n-1]]
    for i in range(1,n):
        if(valid[i]):
            new_ls.append(prefix[i-1]+ls[n-1]-ls[i])
    print(max(new_ls))        
