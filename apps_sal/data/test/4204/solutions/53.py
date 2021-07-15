S = input()
K = int(input())

idx = min(K, len(S))
for s in S[:idx]:
    if s != "1": 
      print(s)
      break
else:
  print(1)
