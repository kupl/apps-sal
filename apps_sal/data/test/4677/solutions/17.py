s = list(input())
w_len = len(s)
word = []
for x in range(w_len):
  if s[x] == 'B':
    if word != []:
      word.pop(-1)
  else:
    word.append(s[x])
result = ''
for y in word:
  result = result+y
print(result)
