li=[0]*5
ans="Yay!"
for i in range(5):
    li[i]=int(input())
k=int(input())

for j in range(5):
    for l in range(5):
        if j<l:
            if k-(li[l]-li[j])<0:
                ans=":("
print(ans)

