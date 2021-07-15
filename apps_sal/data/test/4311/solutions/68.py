s = int(input())

sec = [s]
count = 1
while(s):
  if sec[-1]%2 == 0:
    sec.append(sec[-1]/2)
  else:
    sec.append(3*sec[-1]+1)
  count+=1
    
  if sec[-1] in sec[:-1]:
    print(count)
    break
