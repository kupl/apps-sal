def main():
  N, K = [int(n) for n in input().split(" ")]
  X = [int(x) for x in input().split(" ")]
  X.sort()
  
  minus = []
  plus = []
  for i in range(len(X)):
    if X[i] < 0:
      minus.append(-X[i])
    else:
      plus += X[i:]
      break

  minus.reverse()

  T = []
  
  if len(plus) >= K:
    T.append(plus[K - 1])
  if len(minus) >= K:
    T.append(minus[K - 1])
  for i in range(K):
    if i < len(plus) and 0 <= K - i - 2 < len(minus):
      T.append(2 * plus[i] + minus[K - i - 2])
      T.append(2 * minus[K - i - 2] + plus[i])
    if i < len(minus) and 0 <= K - i - 2 < len(plus):
      T.append(2 * minus[i] + plus[K - i - 2])
      T.append(2 * plus[K - i - 2] + minus[i])
  
  print((min(T)))

main()


