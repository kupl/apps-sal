def main():
  N, M = map(int,input().split())
  fromOne = set()
  toM = set()
  for i in range(M):
    a, b = map(int,input().split())
    if a == 1:
      fromOne.add(b)
    elif b == N:
      toM.add(a)
  return 'POSSIBLE' if fromOne & toM else 'IMPOSSIBLE'
print(main())
