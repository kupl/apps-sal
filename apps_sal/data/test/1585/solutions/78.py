X,Y = map(int,input().split())
a = 1
x = X
mul = min(max(X,2),2)
cnt = 1
for i in range(10000):
  x *= mul
  if x>Y:
    cnt+=i
    break
print(cnt)
