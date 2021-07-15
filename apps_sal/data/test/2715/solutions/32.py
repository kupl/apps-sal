k=int(input())
ans=[0]*50
if k<50:
    for i in range(k):
        ans[i]=50-i
else:
    for i in range(50):
        ans[i]=50-i
    k-=50
    for i in range(50):
        ans[i]+=k//50
    for i in range(k%50):
        ans[i]+=1
print(50)
print(*ans)
