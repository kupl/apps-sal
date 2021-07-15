b,k=map(int,input().split())
A=[int(i) for i in input().split()]
t=0
for i in range(k):
    t+=A[i]*pow(b,k-1-i,2)
    t%=2
if t==0:
    print('even')
else:
    print('odd')
