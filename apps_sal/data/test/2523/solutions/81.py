s = input()
len_s = len(s)
ans = len_s // 2
center = ans
b = s[ans]
if len_s % 2:
  for i in range(center+1):
    if s[center-i] == s[center+i] == b:
      ans += 1
    else:
      break
else:
  for i in range(center):
    if s[center-1-i] == s[center+i] == b:
      ans += 1
    else:
      break
print(ans)

