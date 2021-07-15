n=input()
s=[0 for i in range(10)]
for i in n:
    s[int(i)]+=1

nol=s[0]
del s[0]
#while 0 in s:
#    s.remove(0)
def C(n,k): # C(10,2)=45
    def fact(k):
        s=1
        for i in range(1,k+1):
            s*=i
        return s
    return fact(n)/(fact(k)*fact(n-k))
def var(nol, koeff):
    def C(n,k): # C(10,2)=45
        def fact(k):
            s=1
            for i in range(1,k+1):
                s*=i
            return s
        return fact(n)/(fact(k)*fact(n-k))
    n=0
    if nol!=0:
        koeff.append(nol)
    for i in koeff:
        n+=i
    s=1
    for k in koeff:
        s*=C(n, k)
        n-=k
    if nol!=0:
        koeff.remove(nol)
        nol-=1
        koeff.append(nol)
        s2=1
        n=0
        for i in koeff:
            n+=i
        for k in koeff:
            s2*=C(n,k)
            n-=k
        s-=s2
    return s
c=0
nado=len(s)-s.count(0)
if nol!=0:
    counter=1
else:
    counter=0
for nolik in range(nol+1):
    for c1 in range(s[0]+1):
        for c2 in range(s[1]+1):
            for c3 in range(s[2]+1):
                for c4 in range(s[3]+1):
                    for c5 in range(s[4]+1):
                        for c6 in range(s[5]+1):
                            for c7 in range(s[6]+1):
                                for c8 in range(s[7]+1):
                                    for c9 in range(s[8]+1):
                                        koeff=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
                                        while 0 in koeff:
                                            koeff.remove(0)
                                        if len(koeff)==nado:
                                            if counter==1 and nolik>=1 or counter==0:
                                                c+=var(nolik, koeff)
print(int(c))
