N = int(input())
div = 2
dic = {}
while div**2 <= N:
  if N % div == 0:
    count = 0
    while N % div == 0:
      N = N // div
      count += 1
    dic[div] = count
  div += 1
if N != 1:
  dic[N] = 1
ans = 0
for v in dic.values():
  tmp = 1
  while v >= tmp:
    v -= tmp
    tmp += 1
    ans += 1
print(ans)
