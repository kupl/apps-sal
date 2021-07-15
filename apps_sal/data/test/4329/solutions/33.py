s = input()
t = input()
if(s in t and len(t)==len(s)+1 and t[:len(s)]==s):
  print('Yes')
else:
  print('No')
