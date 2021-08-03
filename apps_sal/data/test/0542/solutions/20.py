n = int(input())
last = 'first'
a = []
b = []
suma = 0
sumb = 0
for i in range(n):
    x = int(input())
    if x > 0:
        last = 'first'
        a.append(x)
        suma += x
    else:
        last = 'second'
        b.append(-x)
        sumb += -x

if suma > sumb:
    print('first')
    quit()
if suma < sumb:
    print('second')
    quit()

for i in range(min(len(a), len(b))):
    if a[i] > b[i]:
        print('first')
        quit()
    elif a[i] < b[i]:
        print('second')
        quit()

if len(a) > len(b):
    print('first')
elif len(a) < len(b):
    print('second')
else:
    print(last)
