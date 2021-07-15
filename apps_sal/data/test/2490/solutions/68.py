s = input()
n = len(s)

ans = 0

sub = 0
judge = False
for i in range(n-1, -1, -1):
  key = int(s[i])+sub
  if key <= 4:
    ans += key
    sub = 0
  elif key == 5:
    ans += 5
    if i == 0:
      sub = 0
    elif int(s[i-1]) <= 4:
      sub = 0
    else:
      sub = 1
  else:
    ans += 10-key
    sub = 1
ans += sub
print(ans)
