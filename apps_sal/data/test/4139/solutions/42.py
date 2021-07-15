N=int(input())
def f(s):
  if int(s)>N:
    return 0
  else:
    ret = 1 if all(s.count(c)>0 for c in "753") else 0
    for c in "753":
      ret+=f(s+c)
    return ret

print(f('0'))
