def sb(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
num=[0]*(10**5+1)
num2=[0]*(10**5+1)
cnt=[0]*(10**5+1)
num[2]+=1
for i in range(2,10**5+1):
    if i%2==1:
        n=sb(i)
        if len(n)==1 and n[0][1]==1:
            num[i]+=1
        if num[i]==1 and num[(i+1)//2]==1:
            num2[i]+=1
for i in range(1,len(num2)):
    cnt[i]=cnt[i-1]+num2[i]
q=int(input())
for i in range(q):
    l,r=list(map(int,input().split()))
    print((cnt[r]-cnt[l-1]))

