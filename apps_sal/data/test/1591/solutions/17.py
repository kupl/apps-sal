n,k=list(map(int,input().split()))
arr = [0]*k
for i in range(n):
    arr[int(input())-1]+=1
shaman=1
ans = 0
for i in range(k):
    ans += (arr[i]//2)*2
    shaman += arr[i]%2
print(ans + (shaman//2))




