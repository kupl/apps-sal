def factorization(n):
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

n=int(input())
ans=0
cnt=[0]
for i in range(1,9):
    for _ in range(i+1):
        cnt.append(i)
lis=factorization(n)


for a,b in lis:
    ans+=cnt[b]
if n==1:
    print((0))
else:print(ans)

