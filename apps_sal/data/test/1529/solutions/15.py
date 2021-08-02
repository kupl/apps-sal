n = int(input())
for i in range(n):
    x = input()
    f = x.endswith('lala.')
    r = x.startswith('miao.')
    if (f and r) or not (f or r):
        print("OMG>.< I don't know!")
    elif f:
        print("Freda's")
    else:
        print("Rainbow's")
