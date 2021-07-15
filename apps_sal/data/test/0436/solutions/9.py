n=int(input())
mas=list(map(int,input().split()))
al=mas[0]
skob=al
skal=al
ans=[1]

for i in range(1,n):
    if mas[i]<=al//2:
        ans.append(i+1)
        skob+=mas[i]
        skal+=mas[i]
    else:
        skob+=mas[i]
if skal*2>skob:
    print(len(ans))
    print(*ans)
else:
    print(0)
