s=list(input())
tmp=0
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        tmp+=1
print(tmp)
