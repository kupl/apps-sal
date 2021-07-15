n = int(input())

a = list(map(int, input().split()))
ans = 0
flag = False
for index, i in enumerate(a, start = 1):
  target = i
  if flag:
    target = a[i-2]

  if index == target:
    ans += 1
    flag = True
  else:
    flag = False
print(ans)
