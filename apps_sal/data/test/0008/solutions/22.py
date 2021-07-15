t = input().split()

t.sort()

if t.count(t[0]) == 3:
  print('0')
elif t.count(t[0]) == 2 or t.count(t[1]) == 2:
  print('1')
else:
  num = list(map(int, [t[0][0], t[1][0], t[2][0]]))
  suit = [t[0][1], t[1][1], t[2][1]]
  if len(set(suit)) == 3:
    print('2')
  elif len(set(suit)) == 1:
    if num[1] == num[0] + 1 or num[2] == num[1] + 1:
      if num[2] == num[0] + 2:
        print('0')
      else:
        print('1')
    elif num[1] == num[0] + 2 or num[2] == num[1] + 2:
        print('1')
    else:
      print('2')
  else:
    if suit[0] == suit[1]:
      if num[1] - num[0] in [1, 2]:
        print('1')
      else:
        print('2')
    elif suit[1] == suit[2]:
      if num[2] - num[1] in [1, 2]:
        print('1')
      else:
        print('2')
    else:
      if num[2] - num[0] in [1, 2]:
        print('1')
      else:
        print('2')
