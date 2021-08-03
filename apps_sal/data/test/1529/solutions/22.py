3

n = int(input())
for _ in range(n):
    s = input()
    if not (s.startswith('miao.') ^ s.endswith('lala.')):
        print("OMG>.< I don't know!")
    elif s.startswith('miao.'):
        print("Rainbow's")
    else:
        print("Freda's")
