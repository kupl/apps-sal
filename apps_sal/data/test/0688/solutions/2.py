t = input()
s = input()
s = list(s)

n = len(s)

copies = 0
x = t.count('6') + t.count('9')
y = s.count('6') + s.count('9')
a = t.count('2') + t.count('5')
b = s.count('2') + s.count('5')
if(x == 0 and a == 0):
    copies = 100
elif(x == 0):
    copies = b // a
elif(a == 0):
    copies = y // x
else:
    copies = min(y // x, b // a)

for j in range(0, 10):
    i = str(j)
    if(i == '6' or i == '9' or i == '2' or i == '5'):
        continue
    x = t.count(i)
    if(x == 0):
        continue
    y = s.count(i)
    copies = min(copies, y // x)

print(copies)
