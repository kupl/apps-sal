def f(s):


  if (len(s) == 1): 
    return 0

  i = len(s)//2

  n = get_max(s, i)

  return max(n, max(f(s[0:i]), f(s[i:len(s)])))



def get_max(s, i):

  j = i-1
  n0 = 0
  n1 = 0

  length = 0

  lmap = {}

  while(j >= 0):
    if s[j] == '0': n0 += 1
    if s[j] == '1': n1 += 1
    length += 1
    lmap[n1-n0] = length
    j -= 1

  j = i
  n0 = 0
  n1 = 0
 
  length = 0

  m = 0

  while(j < len(s)):
    if s[j] == '0': n0 += 1
    if s[j] == '1': n1 += 1
    length += 1
    if((n0-n1) in lmap):
      m = max(m, length+lmap[n0-n1])
    j += 1

  return m

n = input()
s = input()

print(f(s))

