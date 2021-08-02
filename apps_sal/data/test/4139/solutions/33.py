N = int(input())
Nstr = str(N)
Box = ['3', '5', '7']
Boxi = set(Box)
Box = []
Box2 = set()
for _ in range(10**9):
    B = Boxi.pop()
    if len(B) < len(Nstr) and int(B) <= N:
        Boxi.add('3' + B)
        Boxi.add('5' + B)
        Boxi.add('7' + B)
        Box2.add('3' + B)
        Box2.add('5' + B)
        Box2.add('7' + B)
    if Boxi == set():
        break
for i in Box2:
    Bint = int(i)
    if Bint <= N and '3' in i and '5' in i and '7' in i:
        Box.append(Bint)
print(len(Box))
