S = input()
c = 0

bs = '_'
for s in S:
  if s != bs:
    c += 1
    bs = s

print(c - 1)
