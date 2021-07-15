s = input()
a = list()
for item in s:
    ele = int(item)
    a.append(ele)

n = len(s)
for i in range(n):
    a[i] = a[i]%3


one = 0
two = 0
ans = 0

for i in range(n):
    if a[i]==1:
        one+=1
    elif a[i]==2:
        two+=1
    else:
        one = 0
        two = 0
        ans+=1
        continue
    
    if one and two:
        ans+=1
        one = 0
        two = 0
    elif one==3 and two==0:
        ans+=1
        one = 0
        two = 0
    elif two==3 and one==0:
        ans+=1
        one = 0
        two = 0
        
print(ans)
