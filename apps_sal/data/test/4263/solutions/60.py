S = input()

s_len = len(S)
ACGT = {"A", "C", "G", "T"}
max_len = 0
max_str = ''
str = ''

for i in range(s_len):
  str = ''
  for j in range(i, s_len):
    if S[j] in ACGT:
      str += S[j]
      if len(str) >= max_len:
        max_len = len(str)
        max_str = str
    else:
      str = ''


print(max_len)
