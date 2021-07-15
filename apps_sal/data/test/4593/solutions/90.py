X = int(input())
ans = [1]
for i in range(2,X+1):
  p = 2
  while i**p <= X:
    ans.append(i**p)
    p += 1
print(max(ans))
