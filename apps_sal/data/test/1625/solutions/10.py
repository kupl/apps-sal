n=int(input())
a=list(map(float,input().split()))
a.sort(reverse=True)
ans=0
while(a):
    ans += sum(a)
    a=a[:len(a)//4]
print(int(ans))
