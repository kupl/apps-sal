from collections import Counter
s=input()
n=len(s)
ans=0
arr=[0]*(n+1)
if s=='0':
    print(1)
    return
elif n==1:
    print(0)
    return
for i in reversed(range(n)):
    arr[i]=(arr[i+1]+int(s[i])*pow(10,n-i-1,2019))%2019
m=Counter(arr)
for j in m.keys():
    ans+=m[j]*(m[j]-1)//2
print(ans)
