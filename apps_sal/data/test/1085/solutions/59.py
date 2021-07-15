import math
n=int(input())
def s_bunkai(n):
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
num=s_bunkai(n-1)
ans=1
if num[0][0]!=1:
    ans=1
    for i in range(len(num)):
        ans*=num[i][1]+1
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        cnt1=n
        for j in range(50):
            if cnt1%i==0:
                cnt1//=i
                if cnt1==1:
                    ans+=1
                    break
            else:
                if cnt1%i==1:
                    ans+=1
                break
print(ans)

