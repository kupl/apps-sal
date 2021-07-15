n=int(input())
w=list(map(int, input().split()))
s=10000
for i in range(1,n):
  s_1=sum(w[:i])
  s_2=sum(w[i:])
  d=abs(s_1-s_2)
  if d<s:
    s=d
print(s)
