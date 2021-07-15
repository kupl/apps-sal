n,k = map(int,input().split())
s = input()
ms = 0
ps = 0
temp = [0]
if s[0] == "0":
    temp.append(0)
for i in s:
    # print(i,ps,ms)
    if i == "0":
        ms += 1
        if ps:
            temp.append(ps)
            ps = 0
    else:
        ps += 1
        if ms:
            temp.append(ms)
            ms = 0
if ms:
    temp.append(ms)
else:
    temp.append(ps)
# print(temp)
temp.append(0)
for i in range(len(temp)-1):
    temp[i+1] += temp[i]
# print(temp)
ans = 0
if len(temp)-(2*k+1) <= 0:
    ans = temp[-1]
else:
    for i in range(0,len(temp)-(2*k+1),2):
        ans = max(ans,temp[i+2*k+1]-temp[i])
print(ans)
