N, M = [ int(v) for v in input().split(" ") ]
d = []
for i in range(N):
  d.append([ int(v) for v in input().split(" ")])

total = 0
for v, n in sorted(d):
  if M > n:
    total += (v*n)
    M -= n
  else:
    total += (v*M)
    break
    
print(total)
