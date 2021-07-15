n = int(input())
X = list(map(int, input().split()))
x = sorted(X)

res1 = x[n//2]
res2 = x[n//2 -1]

for i in range(n):
  if X[i] >= res1:
    print(res2)
  elif X[i] <= res2:
    print(res1)
