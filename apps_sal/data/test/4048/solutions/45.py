N = int(input())

def low_divisors(N):
  K=1
  low_divs = []
  while K*K <= N:
    if N%K == 0:
      low_divs.append(K)
    K += 1

  return low_divs

L_divs = low_divisors(N)
D = []

for i in range(len(L_divs)):
  D.append(L_divs[i]+N//L_divs[i])
  
print(min(D)-2)
