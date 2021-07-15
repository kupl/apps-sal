x = int(input())
MAX = 10**5+10
res = [0 for i in range(MAX)]
ans = 0

for i in range(2,MAX):
    j = i
    if(res[i] != 0):
        continue
    while(j < MAX):
        if(res[j] == 0):
            res[j] = i
        j += i
        
for i in range(x,MAX) :
    if(res[i] == i):
        ans = i
        break
print(ans)
