n=int(input())
table=[100]*26
for i in range(n):
    k=[0]*26
    s=input()
    for j in s:
        k[ord(j)-97]+=1
    for j in range(26):
        table[j]=min(table[j],k[j])
ans=""
for i in range(26):
    ans+=chr(i+97)*table[i]
print(ans)
