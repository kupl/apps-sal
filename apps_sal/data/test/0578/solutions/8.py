s = input();
l1 = s.find(".")
l2 = s.find("e")

a = s[0:l1]+s[l1+1:l2]
b = int(s[l2+1:len(s)])

for i in range(100):
    a += "0"

a = a[0:l1+b]+"."+a[l1+b:len(a)]

while a[-1] == "0":
    a = a[0:-1]
    
if(a[-1] == "."):
    a = a[0:-1]

print(a)
