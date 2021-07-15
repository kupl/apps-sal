n = int(input())
p = []
for i in range(n):
   p.append(list(input()))
max = 0
for i in range(n):
   q = p
   for t in range(n):
      if q[i][t] == '0':
          for k in range(n):
                 if q[k][t] == '0':
                    q[k][t] = '1'
                 else:
                    q[k][t] = '0'
   col = 0
   for t in range(n):
      sum = 0
      for e in range(n):
         if q[t][e] == '1':
            sum += 1
      if sum == n:
           col += 1
   if col > max:
      max = col
print(max)
      

