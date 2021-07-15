n = int(input())
a = [list(map(lambda x: x - 1, map(int, input().split()))) for i in range(n)]
start = 0
flag = False
ans = []
should_be = -1
while True:
  if start == 0 and flag == True:
    break
  ans.append(start + 1)
  flag = True
  next = a[start][0]
  ok = should_be == -1 or should_be == next
  if ok and (a[start][1] == a[next][0] or a[start][1] == a[next][1]):
    if should_be > -1:
      assert next == should_be
    should_be = a[start][1]
    start = next
    continue
  next = a[start][1]
  ok = should_be == -1 or should_be == next
  if ok and (a[start][0] == a[next][0] or a[start][0] == a[next][1]):
    if should_be > -1:
      assert next == should_be
    should_be = a[start][0]
    start = next
    continue
  assert False
for x in ans:
  print(x, end=' ')

