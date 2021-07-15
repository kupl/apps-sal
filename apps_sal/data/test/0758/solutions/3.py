n=int(input())
B=input()
ans=0
for i in range(n-1,-1,-1):
    ans=ans*2+int(B[i]=='B')
print(ans)

