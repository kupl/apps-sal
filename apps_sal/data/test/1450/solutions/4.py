t = input()
t = t+'2'
Z = []
U = 0
c = 0
for i in t:
    if i=='1':
        U+=1
    elif i=='0':
        c+=1
    else:
        Z.append(c)
        c = 0
for i in range(Z[0]):
    print('0', end='')
for i in range(U):
    print('1', end='')
for j in range(1, len(Z)):
    print('2', end='')
    for i in range(Z[j]):
        print('0', end='')

