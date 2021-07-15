t = input()
d = list(map(int, input().split()))
cure = 0
for i in range(len(d)):
  for s in range(i+1, len(d)):
    cure += d[i] * d[s]
print(cure)
