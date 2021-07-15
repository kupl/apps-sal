n=int(input())
h=list(map(int,input().split()))
a=sum(h)
tmp = 0
for i in range(n):
  tmp += h[i]
  a = min(a, abs(tmp - (sum(h)-tmp)))
print(a)
