X, Y = input().split(' ')
X, Y = int(X), int(Y)
cnt = 1
Num = X
while Num <= Y:
  Num *= 2
  if Num <= Y:
    cnt += 1
print(cnt)
