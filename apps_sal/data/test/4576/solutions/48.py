[a]=[int(i) for i in input().split()]
[b]=[int(i) for i in input().split()]
[c]=[int(i) for i in input().split()]
[x]=[int(i) for i in input().split()]
ans=0
for ia in range(a+1):
    for ib in range(b+1):
        for ic in range(c+1):
            if(ia*500+ib*100+ic*50==x):
                ans+=1
print(ans)

