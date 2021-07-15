K = 10**6
isp = [True] * K
isp[0] = isp[1] = False
for i in range(4, K, 2):
  isp[i] = False
for k in range(3, K, 2):
  if isp[k]:
    j = 2*k
    while j < K:
      isp[j] = False
      j += k

x = int(input())
while True:
  if isp[x]:
    print(x)
    return
  x += 1

