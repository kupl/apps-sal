s=input()
tmp='Bulbasaur'
d={i:0 for i in tmp}
for i in s:
    if i in d:
        d[i]+=1
ans=100000
for i in d:
    chk=d[i]
    if i=='a' or i=='u':
        chk//=2
    ans=min(ans,chk)
print(ans)
