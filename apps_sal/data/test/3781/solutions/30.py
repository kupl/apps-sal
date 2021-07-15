from collections import Counter
t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  c = Counter(a)
  flg = 1
  for i in c.values():
    if i%2:
      flg = 0
  if (flg+n)%2 == 0:
    print("First")
  else:
    print("Second")
