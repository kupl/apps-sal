n = int(input())
ls = list(map(int,input().split()))
cnt = 0
arr =[]
for i in range(n):
 if ls[i]!= 0:
  cnt+=1
 else:
  arr.append(cnt)
  cnt=0
if len(arr)==0:
 print(n)
else:
 print(max(arr))
