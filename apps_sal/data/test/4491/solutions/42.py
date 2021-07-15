N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

nax=0

for i in range(N):
    nax=max(nax,sum(A[:i+1])+sum(B[i:]))
print(nax)
