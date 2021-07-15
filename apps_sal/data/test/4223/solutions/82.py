N=int(input())
S=input()
x=1
for i in range(0,N):
    if i<N-1 and S[i]!=S[i+1] :
        x=x+1
print(x)



