N = int(input())
As = input().split(' ')
As = [int(As[i]) for i in range(N)]
EVEN = 0
for i in range(N):
  if As[i]%2 == 0:
    while As[i]%2 == 0:
      As[i] /= 2
      EVEN += 1
print(EVEN)
