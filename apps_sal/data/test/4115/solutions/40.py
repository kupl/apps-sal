s=input()
cnt=0
l=len(s)-1
for i in range(len(s)//2):
    if s[i]!=s[l-i]:
        cnt+=1
print(cnt)
