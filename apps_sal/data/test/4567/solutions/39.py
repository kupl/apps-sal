N = int(input())
S = [int(input()) for _ in range(N)]
if sum(S)%10 != 0:
  print(sum(S))
else:
  A = sorted(S)
  for i in A:
    if (sum(S)-i)%10 != 0:
      print(sum(S)-i)
      return
  print(0)
