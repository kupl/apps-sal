H, W = [int(i) for i in input().split()]
SS = [input() for _ in range(H)]

def get(lst, i, default=None):
  try:
    return lst[i]
  except IndexError:
    return default

for i in range(H):
  for j in range(W):
    s = SS[i][j]
    if s == '#':
      if '#' not in [get(get(SS, i-1, []), j), get(get(SS, i, []), j-1), get(get(SS, i+1, []), j), get(get(SS, i, []), j+1)]:
        print('No')
        import sys
        return

print('Yes')

