a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
for an in range(a+1):
  for bn in range(b+1):
    for cn in range(c+1):
      if x == 500*an + 100*bn + 50*cn:
        cnt += 1
print(cnt)
