H = int(input())
now = 1
for i in range(1,100):
  if now <= H <= now*2-1:
    print((2**i-1))
    break
  else:
    now *= 2

