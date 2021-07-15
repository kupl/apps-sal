a =int(input())
b = list(map(int,input().split()))
c = []
ans = 0
while b:
  for i in b:
    if i % 2 ==0:
      c.append(i//2)
  b = c
  ans += len(b)
  c = []
print(ans)
