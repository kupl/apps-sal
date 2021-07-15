n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.reverse()
c=[0]*(n+1)
for i in a:
  c[i]+=1 #同じ数がいくつあるか
for i in b:
  c[i]+=1
if max(c)>n:
  print('No')
  return
l=0
while l<n and a[l]!=b[l]: #かぶるまでの数
  l+=1
i=0
while l<n and a[l]==b[l]: #かぶり始めてからかぶり続ける限り
  while a[i]==b[l] or a[l]==b[i]: #i番目と入れ替えてもかぶる場合
    i+=1
  b[i],b[l]=b[l],b[i] #かぶらないことを確認してから入れ替え
  l+=1
print('Yes')
print(' '.join([str(i) for i in b]))
