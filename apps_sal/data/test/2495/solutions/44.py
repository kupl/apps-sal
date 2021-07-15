n = int(input())
lis = list(map(int,input().split()))
cou = 0
co = 0
ans1 = 0
ans2 = 0
for i in range(n):
  cou += lis[i]
  co += lis[i]
  if cou <= 0 and i % 2 == 0:
    ans1 += (1 -cou)
    cou = 1
  if cou >= 0 and i % 2 == 1:
    ans1 += (cou +1)
    cou = -1
  if co >= 0 and i % 2 == 0:
    ans2 += (co +1)
    co = -1
  if co <= 0 and i % 2 == 1:
    ans2 += (1 -co)
    co = 1
print(min(ans1,ans2))
