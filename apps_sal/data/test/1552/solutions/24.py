n = input();
t = input().split()
i1 = []
i2 = []
i3 = []
for i in range(len(t)):
   if t[i]=="1":
      i1.append(i)
   if t[i]=="2":
      i2.append(i)
   if t[i]=="3":
      i3.append(i)
num = min(len(i1),len(i2),len(i3))
print(num)
for i in range(num):
   print(str(i1[i]+1)+" "+str(i2[i]+1)+" "+str(i3[i]+1))

