lst = input().split()
H = int(lst[0])
W = int(lst[1])

field = []
for i in range(H):
   l = []
   s = input()
   for j in range(W):
      l.append(s[j])
   field.append(l)

def count(x, y):
   result = 0
   for P in [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]:
      try:
         if (0 <= P[0]) and (0 <= P[1]) and (field[P[1]][P[0]] == '#'):
            result += 1
      except:
         pass
   return result

for i in range(H):
   for j in range(W):
      if field[i][j] == '.':
         field[i][j] = str(count(j, i))

def list2str(L):
   result = ''
   for t in L:
      result += t
   return result

for I in field:
   print(list2str(I))
