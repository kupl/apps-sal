N, K = map(int, input().split())
A = list(map(int, input().split()))
X = [0 for _ in range(N)]
D = {0: [-1]}
E = {0: 1}
X[0] = (A[0] - 1) % K
if X[0] in D:
  D[X[0]].append(0)
  E[X[0]] += 1
else:
  D[X[0]] = [0]
  E[X[0]] = 1
for i in range(1, N):
  X[i] = (X[i-1] + A[i] - 1) % K
  if X[i] in D:
    D[X[i]].append(i)
    E[X[i]] += 1
  else:
    D[X[i]] = [i]
    E[X[i]] = 1
S = 0
for i in D:
  n = E[i]
  if n > 1:
    L = D[i][:]
    m = L[-1]
    for j in range(n-1):
      x = L[j]
      if m - x < K:
        S += n - 1 - j
      else:
        l, r = j, n
        d = (l + r) // 2
        tmp = 2 * n
        while tmp != 0:
          if L[d] - x <= K - 1:
            l = d
            d = (l + r) // 2
          else:
            r = d
            d = (l + r) // 2
          tmp //= 2
        S += d - j
print(S)
