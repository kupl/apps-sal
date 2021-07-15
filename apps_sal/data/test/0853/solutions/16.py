n = int(input())
a = list(map(int, input().split()))

count0 = 0
count5 = 0
for i in range(n):
  if a[i] == 5:
    count5 += 1
  else:
    count0 += 1

if count0 == 0:
  print(-1)
elif count5 < 9:
  print(0)
else:
  print('5' * (count5 - count5 % 9) + '0' * count0)
