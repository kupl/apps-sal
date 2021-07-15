a = int(input())
b = list(map(int,input().split()))
c = sum(b)
d = 0
ans = abs(c - 2*b[0])
for i in range(a):
  d += b[i]
  c -= b[i]
  ans = min(ans,abs(d-c))
print(ans)


