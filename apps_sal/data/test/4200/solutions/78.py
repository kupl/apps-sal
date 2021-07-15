#ABC161
N,M=map(int,input().split())
A = []
A=[int(x) for x in input().split()]
mini = sum(A)/(4*M)
if M <= len([x for x in A if x >= mini]):
    print('Yes')
else:
    print('No')
