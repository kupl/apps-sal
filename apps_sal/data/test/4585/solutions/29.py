X=int(input())
t=int((2*X)**0.5)+1
ans=0
for i in range(t,0, -1):
    if X <= i*(i+1)/2:
        ans=i
    else:
        break
print(ans)
