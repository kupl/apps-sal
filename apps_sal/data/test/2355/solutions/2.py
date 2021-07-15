import sys

def compute(n,p):
    count=0
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            print('{0} {1}'.format(i,j))
            count += 1
            if(count >= (2*n+p)):
                return

t = int(input())
for case in range(t):
    n,p = list(map(int,input().split()))
    compute(n,p)

