s = input()
x = 0
a = s.count("dream")
b = s.count("dreamer")
c = s.count("erase")
d = s.count("eraser")
reigai1 = s.count("dreamerase")
reigai2 = s.count("dreameraser")
reigai1 = reigai1-reigai2
b = b-reigai1-reigai2
a = a-reigai1-reigai2
c = c-reigai1-reigai2
d = d-reigai2
a2 = a-b
c2 = c-d
# print(a,b,c,d)
# print(a2,c2)
# print(reigai1,reigai2)
# print(a2*5+b*7+c2*5+d*6+reigai1*10+reigai2*11)
if a2*5+b*7+c2*5+d*6+reigai1*10+reigai2*11 == len(s):
    print("YES")
else:
    print("NO")
