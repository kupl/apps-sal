GI = lambda: int(input()); GIS = lambda: list(map(int, input().split())); LGIS = lambda: list(GIS())

def main():
  GI()
  ps = LGIS()
  a = ps[0]
  s = a
  l = [1]
  for i, p in enumerate(ps[1:], 2):
    if p <= a/2:
      s += p
      l.append(i)
  if s > sum(ps) / 2:
    print(len(l))
    print(' '.join(map(str, l)))
  else:
    print(0)

main()

