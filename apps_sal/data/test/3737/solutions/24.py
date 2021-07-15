n = int(input())
data = {
    
}
l = list(map(int,input().split()))
for x in l:
    if x not in data:
        data[x]=0
    data[x]= data[x] + 1
keys = list(data.keys())
keys.sort()
ans = 0
for i in range(1,len(keys)-1):
    ans = ans + data[keys[i]]
    
print(ans)
