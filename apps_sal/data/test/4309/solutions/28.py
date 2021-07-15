A=input()
for i in range(int(A),1000):
   if len(set(str(i)))==1:
      print(i)
      return
