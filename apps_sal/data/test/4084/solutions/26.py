N,A,B=list(map(int,input().split()))
cnt=N//(A+B)
N-=(A+B)*cnt
ans=cnt*A+min(N,A)
print(ans)

