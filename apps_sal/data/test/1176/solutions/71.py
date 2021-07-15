n=int(input())
a=list(map(int,input().split()))

minus_num = 0
for i in range(n):
  if a[i] < 0:
    minus_num += 1

abs_a = list(map(abs,a))
if minus_num % 2 == 0:
  print(sum(abs_a))
else:
  print(sum(abs_a)-2*min(abs_a))
