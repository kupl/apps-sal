import sys

def is_good(lab):
  n = len(lab)
  for i in range(n):
    for j in range(n):
      v = lab[i][j]
      if v > 1 and all(x + y != v for x in lab[i] for y in (lab[k][j] for k in range(n))):
        return False
  return True

n = int(input())

lab = [[int(i) for i in input().split()] for _ in range(n)]

print('Yes' if is_good(lab) else 'No')

