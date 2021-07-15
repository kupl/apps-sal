n=int(input())
p=[int(input()) for i in range(n)]
total=0
for i in range(n):
  total+=p[i]
total-=max(p)*0.5
print(int(total))
