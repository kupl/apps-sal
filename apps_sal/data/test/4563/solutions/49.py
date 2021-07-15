n=int(input())
p,q=1,1

for _ in range(n):
    t,a=map(int,input().split())
    #n=1
    #hile p>n*t or q>n*a:
    #    n+=1
    n=max((p+t-1)//t,(q+a-1)//a)
    p,q=n*t,n*a
    #print(n,p,q)

print(p+q)
