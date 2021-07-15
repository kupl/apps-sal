n=int(input())
s=input()
ans=''
for i in range(len(s)):
    ans+=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
print(ans)
