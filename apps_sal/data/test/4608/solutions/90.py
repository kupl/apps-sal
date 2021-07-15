N = int(input())
a = tuple(int(input()) for _ in range(N))
log = set()
i = 0
count = 1
while a[i] != 2:
  i = a[i] - 1
  if i in log:
    print(-1)
    break
  else:
    log.add(i)
    count += 1
else:
  print(count)
