N=int(input())
*H,=map(int,input().split())
L=len(H)

cnt=0
prv=0

for i in range(N):
    if  prv < H[i]:
        cnt+=H[i]-prv
    prv=H[i]
print(cnt)
