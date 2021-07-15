K = int(input())

a=[7 % K]
for i in range(1, K):
  a.append((10*a[i-1] + 7) % K)

flag = False
for i in range(len(a)):
  if a[i] == 0:
    print((i+1))
    flag = True
    break
if not flag:
  print((-1))

