k=int(input())
def s(n):
    m=str(n)
    l=list(m)
    l=map(int,l)
    return n/sum(l)
p=1
q=0
for i in range(k):
    print(p)
    if s(p+10**q)>s(p+10**(q+1)):
        q+=1
    p+=10**q
