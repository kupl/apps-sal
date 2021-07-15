ac = int(input())
x = set()
y = set()
if ac>0 and ac<100001:
    for i in range(ac):
        a, b = map(int, input().split(' '))
        if a>=0 and a<=100 and b>=0 and b<=100:
            x.add(a)
            y.add(b)
    if len(x)<len(y):
        print(len(x))
    else:
        print(len(y))
