h,w=map(int, input().split())
l=[0]*2*h
for i in range(h):
    c=input()
    l[2*i]=c
    l[2*i+1]=c
    
for i in range(h):
    print(l[2*i])
    print(l[2*i+1])
