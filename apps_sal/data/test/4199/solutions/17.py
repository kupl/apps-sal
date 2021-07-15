n, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
cnt = 0
for hi in h:
  if hi >= k:
    cnt += 1
print(cnt)
