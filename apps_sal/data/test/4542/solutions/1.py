s = input()
cnt = 1
cw = s[0]
for i in range(len(s)):
  if s[i] != cw: 
    cnt += 1
    cw = s[i]
print(cnt - 1)
