O = input()
E = input()

ans = ""
while len(O)>0:
  ans += O[:1]+E[:1]
  O = O[1:]
  E = E[1:]
print(ans)
