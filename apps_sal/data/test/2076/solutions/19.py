t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    ans1=min(a,b//2)
    b1=b-ans1*2
    ans1+=min(b1,c//2)
    ans2=min(b,c//2)
    b-=ans2
    ans2+=min(a,b//2)
    print(max(ans1*3,ans2*3))
