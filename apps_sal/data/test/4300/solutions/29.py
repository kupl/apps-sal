n = int(input())
d = list(map(int,input().split()))
ml = []
for i in range(n):
  for j in range(i+1,n):
    ml.append(d[i]*d[j])
print(sum(ml))
