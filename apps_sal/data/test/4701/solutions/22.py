n=int(input())
k=int(input())
a=1
for _ in range(n):
  if a<k:
    a*=2
  else:
    a+=k
print(a)
