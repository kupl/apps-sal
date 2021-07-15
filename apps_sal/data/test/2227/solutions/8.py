L=list(input().split("heavy"))
ans=0
for i in range(len(L)):
    ans += i*(len(list(L[i].split("metal")))-1)
print(ans)
