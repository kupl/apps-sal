mod = 1000000007
s = str(input())
ans = 1
count1 = 0
arr = []
i = 0
while(i < len(s)):
    if(s[i] == 'b'):
        i += 1
        break
    elif(s[i] == 'a'):
        i += 1
        count1 += 1
    else:
        i += 1
count2 = 0
while(i < len(s)):
    if(s[i] == 'b'):
        if(count2 > 0):
            arr.append(count1)
            count1 = count2
            count2 = 0
    elif(s[i] == 'a'):
        count2 += 1
    i += 1
if(count1 > 0):
    arr.append(count1)
if(count2 > 0):
    arr.append(count2)
for i in range(len(arr)):
    ans = ((ans % mod) * ((arr[i] % mod + 1 % mod) % mod)) % mod
# print(ans,arr)
ans = ((ans % mod - 1 % mod) % mod + mod) % mod
print(ans)
