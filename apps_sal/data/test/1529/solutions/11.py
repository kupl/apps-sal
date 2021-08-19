n = int(input())
for i in range(n):
    sign = False
    sign1 = False
    s = input()
    if s[:5] == 'miao.':
        sign1 = True
    if s[-5:] == 'lala.':
        sign = True
    if sign and sign1 or (sign == False and sign1 == False):
        print("OMG>.< I don't know!")
    elif sign:
        print("Freda's")
    else:
        print("Rainbow's")
