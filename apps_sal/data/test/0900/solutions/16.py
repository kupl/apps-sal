m=10**9+7
s=input()
d=[1]+[0]*12
for i in range(len(s)):
 if s[i]== "?":d=[sum(d[(j-k)*4%13]for k in range(10))%m for j in range(13)]
 else:d=[d[(j-int(s[i]))*4%13]%m for j in range(13)]
print(d[5])
