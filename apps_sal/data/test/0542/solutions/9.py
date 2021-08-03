

n = int(input())

a = []
b = []

first = True
i = 0
j = 0


for i in range(n):
    d = int(input())
    if d > 0:
        a.append(d)
        last = 0
    else:
        b.append(-d)
        last = 1


suma = sum(a)
sumb = sum(b)
if suma > sumb:
    print('first')
elif sumb > suma:
    print('second')
else:
    done = False
    lena = len(a)
    lenb = len(b)
    for i in range(min(lena, lenb)):
        if a[i] > b[i]:
            print('first')
            done = True
            break
        elif a[i] < b[i]:
            print('second')
            done = True
            break
    if not done:
        if lena > lenb:
            print('first')
        elif lenb > lena:
            print('second')
        else:
            if last == 0:
                print('first')
            else:
                print('second')
