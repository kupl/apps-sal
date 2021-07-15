N = int(input())
S = [str(input()) for i in range(N)]
gocha = {}
for s in S:
  gocha[s] = 1
print(len(gocha))
