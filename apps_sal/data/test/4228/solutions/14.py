n,l=list(map(int,input().split()))
aji = []
m = 100000
flg = 0
for i in range(n):
  aji.append((l+i))
  if abs(aji[i]) <= m:
    m = abs(aji[i])
    if aji[i] <= 0:
      flg = 1
    else:
      flg = 0
print((sum(aji)- m if flg==0 else sum(aji) +m))

