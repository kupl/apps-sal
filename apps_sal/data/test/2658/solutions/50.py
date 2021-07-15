N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
check = [0]*N
ima = 0

for i in range(K):
  if check[A[ima]-1] != 0:
    loopen = ima
    check[ima] = i+1
    looplen = check[ima] - check[A[ima]-1] + 1
    loopend = i
    break
  if i == K-1:
    print((A[ima]))
    return
  check[ima] = i+1
  ima = A[ima]-1

offset = (K-(i-looplen)-1)%looplen
ima = 0
for i in range(loopend-looplen+offset+1):
  ima = A[ima]-1
print((ima+1))

