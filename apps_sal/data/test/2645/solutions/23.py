def judge(mygp,yourgp):
  if mygp=='g' and yourgp=='p':
    return -1
  elif mygp=='p' and yourgp=='g':
    return 1
  else:
    return 0

s=[x for x in input()]
t=[['g','p'][x%2] for x in range(len(s))]
print(sum([judge(a,b) for a,b in zip(t,s)]))
