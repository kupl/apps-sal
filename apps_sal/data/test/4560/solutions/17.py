n = int(input())
a = int(input())
cnt = 0
for i in range(21):
  if 0 <= n - i*500 and n - i*500 <= a:
    print("Yes")
    break
  else:
    cnt += 1
    if cnt == 21:
      print("No")
      break
