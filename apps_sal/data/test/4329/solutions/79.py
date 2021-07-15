S = input()
T = input()
result = False
if all([s >= 'a' and s <= 'z' for s in S]):
  if all([t >= 'a' and t <= 'z' for t in T]):
     if len(S) >= 1 and len(S) <= 10:
        if len(T) == len(S) + 1:
          result = T.startswith(S)
if result:
  print('Yes')
else:
  print('No')
