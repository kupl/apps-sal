n=int(input())
s=input().split()
l=[0]+[int(s[i]) for i in range(n)]+[1001]
maxlen=0
prev=0
cnt=1
for i in range(1,n+2):
    if prev==l[i]-1:
        cnt+=1
    else:
        maxlen=max(maxlen,cnt-2)
        cnt=1
    prev=l[i]
maxlen=max(maxlen,cnt-2)
print(maxlen)

