N = int(input())
S = input()

max_count = 0
for i in range(0, N-1):
  X = S[0:i+1]
  Y = S[i+1:]

  X_set = set(X)
  Y_set = set(Y)

  count = len(X_set & Y_set)
  if max_count < count:
    max_count = count

print(max_count)

