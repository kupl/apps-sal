N = int(input())
text = "MARCH"
d = {a:0 for a in text}
for _ in range(N):
  s = input()[0]
  if s in text:
    d[s] += 1

tot = 0
L = [v for k,v in list(d.items())]
for i in range(0,5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      #print(i,j,k)
      tot += L[i]*L[k]*L[j]

#print(d)
print(tot)

