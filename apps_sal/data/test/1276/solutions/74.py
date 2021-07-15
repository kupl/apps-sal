n=int(input())
s=list(input())


ans=(s.count("R"))*(s.count("G"))*(s.count("B"))

for i in range(n) :
    a=s[i]
    for j in range(i+1,n) :
        b=s[j]
        if 2*j-i>n-1 :
            break
        c=s[2*j-i]
        if (a!=b) and (b!=c) and (c!=a) :
            ans-=1

print(ans)
