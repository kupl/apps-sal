s=input()

tmp1 = ''
tmp2 = ''
for i in range(len(s)):
  if i % 2 == 0:
    tmp1 += '0'
    tmp2 += '1'
  else:
    tmp1 += '1'
    tmp2 += '0'

diff_tmp1 = 0
diff_tmp2 = 0
for i in range(len(s)):
  if tmp1[i] != s[i]:
    diff_tmp1 += 1
  elif tmp2[i] != s[i]:
    diff_tmp2 += 1
print(min(diff_tmp1,diff_tmp2))
