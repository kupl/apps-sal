read = lambda : list(map(int,input().split()))

k = int(input())
a = []
s = []
dict = {}
for i in range(k):
   a.append([])
   input()
   s.append(0)
   for j in read():
      s[i] += j
      a[i].append(j)
ok = False
for i in range(k):
   if ok:
      break
   for j  in range(len(a[i])):
      
      x = s[i] - a[i][j]
      tmp = dict.get(x)
      if ( tmp  != None  ):
         ok = True
         print("YES")
         print(i+1,j+1)
         print(tmp[0]+1,tmp[1]+1)
         break

   for j in range(len(a[i])):
      x = s[i] - a[i][j]
      dict[x] = [i,j]
if not ok:
   print("NO")


