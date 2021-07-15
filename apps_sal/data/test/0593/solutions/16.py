n, m = map(int, input().split())
results = [ 0 ] * n
for _ in range(m):
  votes = [ int(vote) for vote in input().split() ]
  maxvote = -1
  winnercity = -1
  for i in range(n):
    if votes[i] > maxvote:
      maxvote = votes[i]
      winnercity = i
  results[winnercity] += 1

maxvote = -1
winnercity = -1
for i in range(n):
  if results[i] > maxvote:
    maxvote = results[i]
    winnercity = i

print(winnercity+1)
