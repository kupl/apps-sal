N, M, X = map(int, input().split(' '))
A, C = [], []
for n in range(N):
  inp = list(map(int, input().split(' ')))
  C.append(inp[0])
  A.append(inp[1:])
  
def proceed_step(remained, current_cost, n):
  nonlocal N, X
  remained_next = []
  
  if not remained: return current_cost
  if n == N: return float('inf')
  
  for algorithm in remained:
    m, current_sum = algorithm[0], algorithm[1]
    current_sum += A[n][m]
    if current_sum < X:
      remained_next.append([m, current_sum])
      
  return min(proceed_step(remained, current_cost, n+1),
             proceed_step(remained_next, current_cost + C[n], n+1))

remained = [[m, 0] for m in range(M)]
total_cost = proceed_step(remained, current_cost=0, n=0)
if total_cost == float('inf'): print(-1)
else: print(total_cost)
