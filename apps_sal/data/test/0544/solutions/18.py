nbChaines = int(input())

for i in range(nbChaines):
   nbCaracteres = int(input())
   chaine = input()
   a = True
   
   for j in range(nbCaracteres//2):
      if ord(chaine[j])-1 == ord(chaine[-1-j])+1 or ord(chaine[j])-1 == ord(chaine[-1-j])-1\
          or ord(chaine[j])+1== ord(chaine[-1-j])-1 or ord(chaine[j])+1== ord(chaine[-1-j])+1:
         pass
      else:
         a = False
   if a:
      print("YES")
   else:
      print("NO")

