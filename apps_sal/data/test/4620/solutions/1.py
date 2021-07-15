N = int(input())

CSF = []
for _ in range(N-1):
  C, S, F = map(int, input().split())
  CSF.append((C, S, F))

def cnt(x):
  ret = 0
  for i in range(x, N-1):
    C, S, F = CSF[i]
    if ret < S:
      ret = S
      ret += C
    else:
      ret = -(-ret//F)*F
      ret += C
  return ret

for x in range(N):
  print(cnt(x))
