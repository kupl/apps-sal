def ain():
    return map(int,input().split())
def lin():
    return list(ain())

def plist(l):
    for x in l:
        print(x, end= ' ')
    print()

a,b,c = ain()
if a > b+c:
    print('+')
elif b > a+c:
    print('-')
elif c == 0 and a==b:
    print('0')
else:
    print('?')
# python3 p.py

