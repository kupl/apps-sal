S = input()
T = input()

n = len(S) - len(T) + 1
min = 1000

if T in S:
  print((0))

else:
  for i in range(n):
    tmp = 0
    for j in range(len(T)):
      if S[i+j] != T[j]:
        tmp += 1
    if tmp < min:
      min = tmp
  print(min)

