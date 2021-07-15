N = int(input())
X = list(map(int, input().split()))
X.sort()

if N == 1:
  print(0)

elif X[0] == X[-1]:
  print(0)

else:
  sum = [0] * (X[-1] - X[0])

  for i in range(X[0],X[-1]):
    for j in X:
      sum[i - X[0]] += (j - i ) ** 2

  print(min(sum))
