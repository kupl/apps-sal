S = input()
L = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','C']
con = 0
for i in range(len(S)):
  if i == 0:
    if S[0] != 'A':
      print('WA')
      return
  elif i == len(S) - 1 or i == 1:
    if S[i] not in L or S[i] == 'C':
      print('WA')
      return
  else:
    if S[i] not in L:
      print('WA')
      return
    if S[i] == 'C':
      con += 1
      if con >= 2:
        print('WA')
        return
if con == 0:
  print('WA')
  return
else:
  print('AC')
