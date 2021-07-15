N,A,B=map(int,input().split())
print(N//(s:=A+B)*A+min(N%s,A))
