#ABC124 D-Handstand
n,k = map(int,input().split())
s = []
count = 0
last = 1
for i in input():
    if i=='1':
        if last==1:
            count+=1
        else:
            s.append(count)
            count=1
        last = 1
    else:
        if last==0:
            count+=1
        else:
            s.append(count)
            count=1
        last = 0
s.append(count)
if last==0:
    s.append(0)

k = min(k,len(s)//2)
ans = 0

for j in range(len(s)//2-k+1):
    if j==0:
        now = sum(s[:k*2+1])
        ans = now
    else:
        now = now-s[j*2-1]-s[j*2-2]+s[(j+k)*2]+s[(j+k)*2-1]
        ans = max(ans,now) 
print(ans)
