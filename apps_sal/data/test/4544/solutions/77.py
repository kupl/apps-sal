N=int(input())
a=list(map(int, input().split(" ")))
#print(a)
sums=[0]*(10**5)
#print(sums)

for val in a:
  #print(val)
  if val-1>=0:
    sums[val-1]=sums[val-1]+1
  sums[val]=sums[val]+1
  if val+1<10**5:
    sums[val+1]=sums[val+1]+1

print(max(sums))
