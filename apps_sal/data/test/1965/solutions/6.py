t = int(input())
for _ in range(t):
  n, x = [int(i) for i in input().split(" ")]
  a = [int(i) for i in input().split(" ")]
  diff = sum(a) - n*x
  if diff == 0:
    if max(a) == min(a):
      print(0)
    else:
      print(1)
  else:
    if x in a:
      print(1)
    else:
      print(2)
