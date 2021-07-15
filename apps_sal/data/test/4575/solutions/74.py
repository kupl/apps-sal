n=int(input())
d,x=map(int,input().split())
ans=x
for i in range(n):
  ans += (d-1)//int(input())+1
print(ans)
