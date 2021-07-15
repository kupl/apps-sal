S = input()

flag = 1
c_count = 0
if S[0] == 'A':
  for i in range(1,len(S)):
    if 2 <= i <= len(S)-2:
      if S[i] == 'C':
        c_count += 1
    else:
      if S[i].islower() == False:
        flag = 0
else:
  flag = 0
if c_count == 1 and flag == 1:
  print('AC')
else:
  print('WA')
