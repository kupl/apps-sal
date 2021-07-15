n=int(input())

a=list(map(int,input().split()))

m=sum(a[0::2])-sum(a[1::2])

M=[m]

for i in range(n-1):
    M.append(2*a[i]-M[i])

print(*M)
