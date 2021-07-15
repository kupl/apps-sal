n=int(input())
s=set()
m={"purple":"Power","green":"Time","blue":"Space","orange":"Soul","red":"Reality","yellow":"Mind"}
l=[ 'purple', 'green', 'blue', 'orange', 'red', 'yellow']
for i in range(n):
      ch=input()
      s.add(ch)
l1=[]
for i in l:
      if i not in s:
            l1.append(i)
print(len(l1))
for i in l1:
      print(m[i])

