n=int(input())
d=int(input())
e=int(input())*5

ans=10**8+1
for i in range(d):
    k=n-e*i
    if k<0:
        break
    ans=min(ans, k%d)

print(ans)
