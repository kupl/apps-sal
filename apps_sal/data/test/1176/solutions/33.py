n = input()
a = list(map(int, input().split()))
m = 0
for i in a:
  if i < 0:
    m += 1
b = list(map(abs, a))
if m % 2 == 0:
  print(sum(b))
else:
  print(sum(b) - 2*min(b))
