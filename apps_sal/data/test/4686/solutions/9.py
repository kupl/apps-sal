S = input()

P = set()
for s in S:
  if s not in P and S.count(s)%2 != 0:
    print("No")
    return
  P.add(s)
print("Yes")
