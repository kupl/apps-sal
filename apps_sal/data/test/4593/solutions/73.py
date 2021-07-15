X = int(input())
ans = []
for i in range(1,X+1):
  A = 0
  p = 2
  if i == 1:
    ans.append(1)
  else:
    while True:
      A = i**p
      if A <= X:
        ans.append(A)
        p += 1
      else:
        break
print(max(ans))
