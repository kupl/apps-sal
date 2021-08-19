n = int(input())
for i in range(n):
    s = input()
    f1 = 0
    f2 = 0
    if len(s) >= 5 and s[-5:] == 'lala.':
        f1 = 1
    if len(s) >= 5 and s[:5] == 'miao.':
        f2 = 1
    if f1 and f2 or (f1 == 0 and f2 == 0):
        print("OMG>.< I don't know!")
    elif f1 == 1:
        print("Freda's")
    else:
        print("Rainbow's")
