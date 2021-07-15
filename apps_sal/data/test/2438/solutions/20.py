import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
s = input()[:-1]

ans = 0

i = 0
arr = [0]
prefix = [0,0]
while i < len(s):
    n = s[i]
    cnt = 0
    while i < len(s) and n == s[i]:
        cnt+=1
        i+=1
    arr.append(cnt)
    prefix.append(prefix[-1]+cnt)
    
ans = 0
#print(prefix)
for i in range(len(arr)-1):
    #print(arr[i+1], prefix[i], prefix[i+1])
    ans+=arr[i+1]*prefix[i+1]
    #print(ans, end = " ")
    ans-=arr[i]
    if prefix[i+1] > 0:
        ans-=(arr[i+1]-1)
    ans += ((arr[i+1]*(arr[i+1]-1))//2)
    #print(ans)
print(ans)







