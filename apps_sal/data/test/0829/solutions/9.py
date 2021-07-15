n = int(input())
a = input()

z = 0
o = 0
for i in a:
    if i=='0':
        z+=1
    else:
        o+=1
if z!=o:
    print(1)
    print(a)
else:
    print(2)
    print(a[0], a[1:])

