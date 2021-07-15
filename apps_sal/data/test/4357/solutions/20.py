A,B,C = map(int,input().split())
ans = 0
if(A>=B and A>=C):
    ans = max(A*10+B+C,ans)
if(B>=A and B>=C):
    ans = max(B*10+A+C,ans)
else:
    ans = max(C*10+A+B,ans)
print(str(ans))
