N = int(input())
W = list(map(int, input().split()))

S1 = 0
S2 = W[N - 1]
i = 0
j = 2

while True:
  if i > N - j:
    print(abs(S1-S2))
    break
  if S1 <= S2:
    S1 = S1 + W[i]
    i = i + 1
  else:
    S2 = S2 + W[N - j]
    j = j + 1
