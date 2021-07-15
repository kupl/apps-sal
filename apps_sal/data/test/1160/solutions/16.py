d = dict.fromkeys(['S', 'M', 'L', 'XL', 'XXL', 'XXXL'])
d2 = {'S': 0, 'M': 0, 'L': 0, 'XL': 0, 'XXL': 0}
d3 = {'S': 0, 'M': 0, 'L': 0, 'XL': 0, 'XXL': 0, 'XXXL': 0}
l = input().split()
l2 = []
i = 0
for x in ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']:
  d[x] = int(l[i])
  i += 1

n = int(input())
t = True
for i in range(n):
  l = input().split(',')
  l2 += [l]
  if len(l) == 1:
    d[l[0]] -= 1
    if d[l[0]] < 0:
      print('NO')
      t = False
      break
  else:
    d2[l[0]] += 1
m = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
if t == True:    
  for i in range(5):
    if d[m[i]] >= d2[m[i]]:
      d3[m[i]] += d2[m[i]]
      d[m[i]] -= d2[m[i]]
    else:
      d3[m[i]] += d[m[i]]
      d[m[i+1]] -= (d2[m[i]] - d[m[i]])
      d[m[i]] = 0
      if d[m[i+1]] < 0:
        print('NO')
        t = False
        break
if t == True:
  print('YES')
  for x in l2:
    if len(x) == 1:
      print(x[0])
    else:
      if d3[x[0]] > 0:
        print(x[0])
        d3[x[0]] -= 1
      else:
        print(x[1])
      
    
      


