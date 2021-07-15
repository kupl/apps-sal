n,k=list(map(int,input().split()))
S=input()
c,row_count=S[0],1

for s in S:
  if c != s:
    c = s
    row_count += 1

if row_count-k*2 <= 1:
  row_count = 1
else:
  row_count -= k*2
  
print(n-row_count)
