import sys

#ist s1 ein substring von s2, d.h. sind alle Buchstaben von s1 in s2 enthalten?
def substring(s1,s2):
  s2copy = list(s2)
  s1copy = list(s1)
  for i in s1copy:
    try:
      s2copy.remove(i)
    except:
      #print(i,s2copy)
      return False
  return True 

#ist s1 ein sortedsubstring von s2, d.h. kann man durch löschen von Buchstaben s1 aus s2 erzeugen?
def sortedsubstring(s1,s2):
  if not substring(s1,s2):
    return False #nicht mal substring
  s2copy = s2[:]
  s1 
  for i in s1:
    pos = s2copy.find(i)
    if pos == -1:
      return False
    s2copy = s2copy[(pos+1):]
  return True
 
words = sys.stdin.read().splitlines()
sorted0 = list(words[0])
sorted0.sort()
sorted1 = list(words[1])
sorted1.sort()

if not substring(words[1],words[0]):
  print("need tree")
elif sortedsubstring(words[1],words[0]):
  print("automaton")
elif sorted0 == sorted1:
  print("array")
else:
  print("both")

 

