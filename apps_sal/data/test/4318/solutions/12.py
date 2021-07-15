N=int(input())
H=list(map(int,input().split()))
x=1
for i in range(N):
    for j in range(i):
        if H[i]<H[j]:
            break
        if j==i-1:
            x+=1
print(x)
