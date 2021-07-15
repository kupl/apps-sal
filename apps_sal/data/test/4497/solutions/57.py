n = int(input())

cnt = 0
while n > 0:
  n = n // 2
  if n != 0:
    cnt += 1
print(2 ** cnt)
