(a,b)=map(int, input().split())
if a%2==0:
    s=[0]*a
    for i in range(a):
        s[i]=[0]*b
        s[i]=list(map(int, input().split()))
    while s[:a//2]==s[:a//2-1:-1] and len(s)>1:
        a=a//2
        s=s[:a]
else:
    for i in range(a):
        n=input()
print(a)      
