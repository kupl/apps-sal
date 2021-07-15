N = int(input())
d = {}
dupli = 0
for _ in range(N):
  i = input()
  if i in d:
    d[i] += 1
    dupli += 1
  else:
    d[i] = 0
print(str(N-dupli))
