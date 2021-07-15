x, y = map(int,input().split())
S1 = [1, 3, 5, 7, 8, 10, 12]
S2 = [4, 6, 9, 11]
ans = False
for i in range(len(S1)):
  for j in range(len(S1)):
    if S1[i] == x and S1[j] == y:
      ans = True
for i in range(len(S2)):
  for j in range(len(S2)):
    if S2[i] == x and S2[j] == y:
      ans = True
if ans:
  print("Yes")
else:
  print("No")
