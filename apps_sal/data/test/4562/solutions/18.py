N=int(input())
ans=1
for i in range(N+1):
    if i*i<=N:
        ans=i
    else:
        break
print((ans**2))

