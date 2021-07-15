N = int(input())
ans = (N//11)*2
nokori = N%11
if nokori == 0:
  ans += 0
elif nokori <= 6:
  ans += 1
else:
  ans += 2
print(ans)
