def main():
  ss = input().split(';')
  s = []
  for word in ss:
    s.extend(word.split(','))

  a = []
  b = []

  for word in s:
    if word.isdecimal() and ( len(word) > 1 and word[0] != '0' or len(word) == 1):
      a.append(word)
    else:
      b.append(word)

  print('"' + ','.join(a) + '"' if len(a) else '-')
  print('"' + ','.join(b) + '"' if len(b) else '-')



#help(str)
main()
