N=int(input())
two=[2**i for i in range(7)]
ans=max([x for i,x in enumerate(two) if x<=N])
print(ans)
