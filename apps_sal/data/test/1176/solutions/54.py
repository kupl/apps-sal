n = int(input())
a = list(map(int, input().split()))
b = min(a,key=abs)
c = 0
sum_abs_a = 0
for i in range(n):
  sum_abs_a += abs(a[i])
for i in a:
  if i < 0:
    c += 1
if c % 2 == 0:
  print(sum_abs_a)
else:
  print((sum_abs_a - abs(b)*2))



