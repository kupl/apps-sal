a=[int(i) for i in input().split()]
k=int(input())

sum_a=sum(a)

ans=sum_a-max(a)+max(a)*2**k

print(ans)
