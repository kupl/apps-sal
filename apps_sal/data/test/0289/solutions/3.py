s=str(input())
m=s.count('VK')
for i in range(len(s)):
    if s[i]=='V':
        t='K'
    else:
        t='V'
    temp=s[:i]+t+s[i+1:]
    #print(temp)
    if temp.count('VK')>m:
        m=temp.count('VK')
print(m)

