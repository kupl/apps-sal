N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
vc = 0

for j in range(N):
  if V[j] - C[j] > 0:
    vc = vc +( V[j] - C[j] )

print(vc)
