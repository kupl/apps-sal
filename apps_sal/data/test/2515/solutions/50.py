table=[True for i in range(100000+1)]
table[0]=False
table[1]=False
for i in range(2,100000+1):
    for j in range(2,100000//i+1):
        table[i*j]=False
cnt=[0 for _ in range(100000+1)]
for i in range(1,100000+1):
    cnt[i]=cnt[i-1]
    if i%2==1 and table[i]==True and table[(i+1)//2]==True:
        cnt[i]+=1

Q=int(input())
lr=[list(map(int,input().split())) for _ in range(Q)]
for i in range(Q):
    print((cnt[lr[i][1]]-cnt[lr[i][0]-1]))

