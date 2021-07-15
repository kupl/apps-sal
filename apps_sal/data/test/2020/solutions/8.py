I=input
a=set()
b=set()
for _ in '0'*int(I()):x,y=I().split();a.add(x);b.add(y)
print(min(len(a),len(b)))
