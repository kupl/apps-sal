n=int(input())
anst,ansa=map(int,input().split())
for _ in range(1,n):
    t,a=map(int,input().split())
    if anst>t or ansa>a:
        mul=max(-(-anst//t),-(-ansa//a))
        anst=mul*t
        ansa=mul*a
    else:
        anst=t
        ansa=a
print(anst+ansa)
