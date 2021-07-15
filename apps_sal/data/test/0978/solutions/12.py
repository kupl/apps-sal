k=int(input())
g=''
for i in range(4):
    g = g+input()
#print(g)
valid=True
for i in range(1,10):
    if g.count(str(i))>2*k:
        valid=False
        break
if valid:
    print('YES')
else:
    print('NO')

