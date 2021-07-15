Cooky = list(map(int, input().split()))
ans = 'No'
for i in range(1,15):
  tmp = str(bin(i))
  tmp = tmp[2:]
  if len(tmp) != 4:
    tmp = '0'*(4-len(tmp))+tmp
  sum1, sum2 = 0, 0
  for j in range(4):
    if tmp[j] == '1':
      sum1 += Cooky[j]
    else:
      sum2 += Cooky[j]
  if sum1 == sum2:
    ans = 'Yes'
    break
print(ans)
