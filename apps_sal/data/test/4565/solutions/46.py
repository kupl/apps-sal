n=int(input())
s=input()

dp_w=[0]
dp_e=[0]

for i in range(n):
    if i!=0:
        dp_w.append(dp_w[-1])
        dp_e.append(dp_e[-1])
    if s[i]=="W":
        dp_w[-1]+=1
    else:
        dp_e[-1]+=1

def migi(i):
    if i==n-1:
        return 0
    return dp_e[n-1]-dp_e[i]
def hidari(i):
    if i==0:
        return 0
    return dp_w[i-1]
ans=1000000000000000
for i in range(n):
    right=migi(i)
    left=hidari(i)
    ans=min(right+left,ans)
print(ans)
