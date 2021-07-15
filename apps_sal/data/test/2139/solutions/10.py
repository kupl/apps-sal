from sys import stdin
debug = False

try :
  import os
  if os.environ['COMPUTERNAME'] == 'KRUEGER-PC':
    debug = True
except KeyError:
  pass  

def debug_print(*foo):
  if debug:
    print (foo)

debug_print("debug active")    

def print_array(res, size):
  if size:
    print(len(res))
  print(" ".join(map(str, res)))

def input_int_tuple():
  return tuple([ x for x in map(int, stdin.readline().split())])

def input_int_array(size=True):
  if size:
    #read 
    values = stdin.readline().split()
    assert(len(values) == 1)
  return [x for x in map(int, stdin.readline().split())]

def input_string():
  return stdin.readline().strip()



def problem():
  import re
  bear = "bear"
  s  = input_string()

  diffs = []
  prev = 0
  cnt = 0
  for m in re.finditer( bear, s ):
      cnt +=1
      diffs.append(m.start() - prev )
      prev = m.end()

  if cnt >0:
    diffs.append(len(s) - prev)
  else:
    return 0
    


  res = 0
  for i,v in enumerate(diffs):
    if i > 0 :
      v += 3
    if i < len(diffs) -1 :
      v += 3

    res += (v*v -v) // 2 +v
  
  cor = (len(diffs)-1)*3
  res = res - cor
  n = len(s)
  return (n*n-n) // 2 + n -  res 


 


print(problem()) 


#print_array(problem(), False)

#xx = input_string()

