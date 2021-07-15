n = int(input())
A = list(map(int,input().split()))
B = [abs(a) for a in A]
ans=sum(B)
c=sum(1 for a in A if a<0)
if c%2 :
    ans-=min(B)*2
print(ans)

