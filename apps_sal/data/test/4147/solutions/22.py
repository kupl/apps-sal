N, A, B, C = map(int, input().split())
L = []
for _ in range(N):
  L.append(int(input()))

def rec(i, a, b, c):
  if i == N:
    if not a or not b or not c: return float('inf')
    return abs(a-A) + abs(b-B) + abs(c-C)
  
  ret = rec(i+1, a, b, c)
  
  ret = min(ret, rec(i+1, a+L[i], b, c) + (10 if a else 0))
  ret = min(ret, rec(i+1, a, b+L[i], c) + (10 if b else 0))
  ret = min(ret, rec(i+1, a, b, c+L[i]) + (10 if c else 0))
  
  return ret

print(rec(0, 0, 0, 0))
