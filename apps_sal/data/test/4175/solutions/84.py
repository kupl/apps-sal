a = int(input())
l = []
for i in range(a):
    l.append(input())
head = l[0][0]
c = 0
if len(l) != len(set(l)):
    print('No')
    exit
else:
    for i in l:
        if i[0] != head:
            print('No')
            break
        else:
            head = i[-1]
            c += 1
if c == a:
    print('Yes')
