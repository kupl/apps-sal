n=int(input())
h=list(map(int, input().split()))
count=0
for i in range(n):
  check=True
  for j in range(i):
    if h[j]>h[i]:
      check=False
  if check:
    count+=1
print(count)
