n,k=map(int,input().split())
arr=sorted(list(input().strip()))
curr=0
ans=[ord(arr[0])-ord("a")]
for i in arr:
  if ord(i)-ord("a")-ans[len(ans)-1]>=2:
    ans.append(ord(i)-ord("a"))
if len(ans)<k:
  print(-1)
else:
  print(sum(ans[:k])+k)
