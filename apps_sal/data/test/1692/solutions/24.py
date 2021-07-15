s=str(input())
count=0
if int(s[0])%4==0:
    count+=1
for i in range(1,len(s)):
    if int(s[i])%4==0:
        count+=1
    if int(s[i-1:i+1])%4==0:
        count+=1
        count+=i-1
print(count)

