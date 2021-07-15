n=int(input())
h=list(map(int,input().split()))
ans=[]
for i in range (n):
    s=0
    for y in range (n):
        s+=(abs(i-y)+y+i+i+y+abs(i-y))*h[y]
    ans.append(s)
print(min(ans))

