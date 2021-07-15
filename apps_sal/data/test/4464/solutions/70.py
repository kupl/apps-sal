ans = 'NO'
a, b, c = map(int, input().split())
memo = []
for i in range(1, 10**9):
  tmp = (a * i)%b
  if tmp == c:
    ans = 'YES'
    break
  if tmp in memo:
    break
  else:
    memo.append(tmp)
print(ans)
