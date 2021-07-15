from sys import stdin,stdout
n=int(stdin.readline().strip())
for t in range(n):
    h,c=list(map(int,stdin.readline().strip().split()))
    ans=0
    if c!=0:
        ans+=60-c
        h+=1
    ans+=(24-h)*60
    print(ans)
        


