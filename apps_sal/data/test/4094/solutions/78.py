k = int(input())
start = 7 % k
ans = start
con = 1

if k % 2 == 0 or k % 5 == 0:
  print("-1")
  return
while True:
  if ans == 0:
    print(con)
    break
  else:
    con += 1
    ans = ans * 10 + 7
    ans = ans % k
    if ans == start:
      print("-1")
      break

