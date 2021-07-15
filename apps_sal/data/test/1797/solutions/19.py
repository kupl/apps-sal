n = int(input())
p = [0] + list(map(int, input().split()))

def visit(v):
  res = 0
  while p[v] != 0:
    res += 1
    x = p[v]
    (p[v], v) = (0, x)    
  return res 

val = sorted([visit(v) for v in range(n + 1)])
print(sum(list(map(lambda x: x*x, val))) + 2 * val[-1] * val[-2])
