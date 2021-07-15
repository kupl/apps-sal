n=int(input())
a=list(map(int, input().split()))
d=0
for i in a:
  d+=1/i
print(1/d)
