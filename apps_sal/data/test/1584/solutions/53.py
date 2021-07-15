from bisect import bisect_left
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(n):#一番短い棒
  for j in range(i+1,n):#二番目に短い棒
    #1+2番目の棒の長さより短く、2番目に短い棒より長い棒の範囲を探す
    ans += bisect_left(l,l[i]+l[j])-(j+1)
print(ans)
