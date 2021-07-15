N = int(input())
D = [list(map(int, input().split())) for i in range(N)]

k = 0
for d in D:
  if d[0] == d[1]:
    k += 1
    if k >= 3:
      print("Yes")
      return
  else:
    k = 0

print("No")

