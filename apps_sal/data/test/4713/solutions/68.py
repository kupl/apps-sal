n = int(input())
s = input()
ans = 0
x = 0
for i in s:
  if i == 'I':
    x += 1
  else:
    x -= 1
  if x > ans:
    ans = x
print(ans)
